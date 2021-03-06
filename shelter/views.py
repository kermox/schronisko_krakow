from django.http import QueryDict
from django.urls import reverse
from django.views.generic import DetailView, FormView, TemplateView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView, MultipleObjectMixin

from mails.forms import EmailForm
from mails.models import EmailAddress
from mails.tasks import send_email

from .forms import SearchAnimalForm
from .models import Animal, ShelterGallery


class HomePageView(TemplateView, MultipleObjectMixin):
    model = Animal
    template_name = 'shelter/home.html'
    extra_context = {
        'home_page': 'active'
    }
    context_object_name = 'animals'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePageView, self).get_context_data(object_list=self.get_queryset(), **kwargs)
        context['adopted_animals'] = self.get_queryset().filter(adopted=True)
        context['not_adopted_animals'] = self.get_queryset().filter(adopted=False)
        context['shelter_gallery'] = ShelterGallery.objects.first()
        return context

    def get_queryset(self):
        super(HomePageView, self).get_queryset()
        queryset = Animal.objects.all()
        return queryset





class AnimalListView(FormMixin, ListView):
    model = Animal
    template_name = 'shelter/animal-list.html'
    form_class = SearchAnimalForm
    paginate_by = 6
    extra_context = {
        'animal_list_page': 'active',
    }

    def get_queryset(self):
        """
        Returns a filtered queryset after submitting a form with GET request.
        """
        super(AnimalListView, self).get_queryset()
        # get data from request
        data = self.request.GET.copy()
        # create new QueryDict
        q = QueryDict(mutable=True)
        # update QueryDict with key:value from data
        for key, value in data.items():
            if value != '' and key != 'page':
                if key == 'age':
                    if value == 0:
                        q.update({f'{key}__lte': 1})
                    elif value == 1:
                        q.update({f'{key}__range': [1, 3]})
                    elif value == 2:
                        q.update({f'{key}__range': [3, 5]})
                    elif value == 3:
                        q.update({f'{key}__gte': 5})
                    else:
                        q.update({key: value})
                else:
                    q.update({key: value})
        # filter queryset with new QueryDict
        animal = Animal.objects.filter(**q.dict(), adopted=False).order_by('name')
        return animal


class AnimalDetailPOST(SingleObjectMixin, FormView):
    """
    This view is called when user submits an email form.
    """
    template_name = 'shelter/animal-detail.html'
    form_class = EmailForm
    model = Animal

    def get_success_url(self):
        return reverse('animal-detail', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            address = form.cleaned_data['address']
            # if form is valid, send an email
            send_email.delay(address)
            return self.form_valid(form)
        else:
            return self.form_class()

    def form_valid(self, form):
        if form.cleaned_data['address'] \
                and form.cleaned_data['address'] not in [i.address for i in EmailAddress.objects.all()]:
            form.save()
        return super(AnimalDetailPOST, self).form_valid(form)


class AnimalDetailGET(DetailView):
    model = Animal
    template_name = 'shelter/animal-detail.html'
    context_object_name = 'animal'

    def get_context_data(self, **kwargs):
        context = super(AnimalDetailGET, self).get_context_data(**kwargs)
        context['form'] = EmailForm()
        context['animal_detail_page'] = 'active'
        return context


class AnimalDetail(View):
    """
    Calls an appropriate view for POST and GET request.
    """
    def get(self, request, *args, **kwargs):
        # Thanks to flash message we are preventing user from submitting the same form twice after reloading the page.
        flash_message = request.session.get('flash_message', False)
        if flash_message:
            del(request.session['flash_message'])
        # When user requests a page for the first time flash_message is set to False and is passed to AnimalDetailGET
        # view as extra_content.
        view = AnimalDetailGET.as_view(extra_context={'flash_message': flash_message})
        return view(request, *args, **kwargs, )

    def post(self, request, *args, **kwargs):
        # When user send a POST request, the flash_message is set to True.
        request.session['flash_message'] = True
        view = AnimalDetailPOST.as_view()
        return view(request, *args, **kwargs)
