from django.urls import path

from .views import HomePageView, AnimalDetailView, AnimalListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('animal-list/', AnimalListView.as_view(), name='animal-list'),
    path('results/<slug:slug>/', AnimalDetailView.as_view(), name='animal-detail'),
]
