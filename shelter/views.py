from django.http import QueryDict

from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin

from .forms import SearchAnimalForm
from .models import Animal


class HomePageView(TemplateView):
    template_name = 'shelter/home.html'


class AnimalListView(FormMixin, ListView):
    model = Animal
    template_name = 'shelter/animal-list.html'
    form_class = SearchAnimalForm
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        data = self.request.GET.copy()
        q = QueryDict(mutable=True)
        for key, value in data.items():
            if value != '' and key != 'page':
                q.update({key: value})
        animal = Animal.objects.filter(**q.dict())
        return animal


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'shelter/animal-detail.html'


