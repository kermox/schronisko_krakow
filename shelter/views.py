from django.http import QueryDict
from django.urls import reverse

from django.views.generic import TemplateView, DetailView, FormView, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin

from .forms import SearchAnimalForm
from .models import Animal

from mails.forms import EmailForm
from mails.models import EmailBase
from mails.tasks import send_email


class HomePageView(TemplateView):
    template_name = 'shelter/home.html'
    extra_context = {
        'home_page': 'active'
    }


class AnimalListView(FormMixin, ListView):
    model = Animal
    template_name = 'shelter/animal-list.html'
    form_class = SearchAnimalForm
    paginate_by = 6
    extra_context = {
        'animal_list_page': 'active',
    }

    def get_queryset(self):
        super(AnimalListView, self).get_queryset()
        data = self.request.GET.copy()
        q = QueryDict(mutable=True)
        for key, value in data.items():
            if value != '' and key != 'page':
                q.update({key: value})
        animal = Animal.objects.filter(**q.dict()).order_by('name')
        return animal


class AnimalDetailPOST(SingleObjectMixin, FormView):
    template_name = 'shelter/animal-detail.html'
    form_class = EmailForm
    model = Animal

    def get_success_url(self):
        return reverse('animal-detail', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            address = form.cleaned_data['email_address']
            send_email.delay(address)
            return self.form_valid(form)
        else:
            return self.form_class()

    def form_valid(self, form):
        if form.cleaned_data['email_address'] \
                and form.cleaned_data['email_address'] not in [i.email_address for i in EmailBase.objects.all()]:
            form.save()
        return super(AnimalDetailPOST, self).form_valid(form)


class AnimalDetailGET(DetailView):
    model = Animal
    template_name = 'shelter/animal-detail.html'
    context_object_name = 'animal'
    extra_context = {
        'animal_detail_page': 'active',
    }

    def get_context_data(self, **kwargs):
        context = super(AnimalDetailGET, self).get_context_data(**kwargs)
        context['form'] = EmailForm()
        return context


class AnimalDetail(View):

    def get(self, request, *args, **kwargs):
        flash_message = request.session.get('flash_message', False)
        if flash_message:
            del (request.session['flash_message'])
        view = AnimalDetailGET.as_view(extra_context={'flash_message': flash_message})
        return view(request, *args, **kwargs, )

    def post(self, request, *args, **kwargs):
        request.session['flash_message'] = True
        view = AnimalDetailPOST.as_view()
        return view(request, *args, **kwargs)
