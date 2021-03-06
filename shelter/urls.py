from django.urls import path

from .views import AnimalDetail, AnimalListView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('animals/', AnimalListView.as_view(), name='animal-list'),
    path('animals/<slug:slug>/', AnimalDetail.as_view(), name='animal-detail'),
]
