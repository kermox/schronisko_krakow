from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import QueryDict

from .forms import SearchAnimalForm
from .models import Animal


class HomePageView(TemplateView):
    template_name = 'shelter/base.html'


class SearchFormView(View):
    model = Animal
    form_class = SearchAnimalForm
    template_name = 'shelter/search.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {
            'form': form,
        })

    def post(self, request, *arg, **kwargs):
        form = self.form_class(request.POST)
        data = request.POST.copy()
        q = QueryDict(mutable=True)
        for key, value in data.items():
            if value != '' and key != 'csrfmiddlewaretoken' and value != '-----':
                q.update({key: value})
        animal = Animal.objects.filter(**q.dict())
        return render(request, self.template_name, {
            'animal': animal,
            'form': form,
        })
