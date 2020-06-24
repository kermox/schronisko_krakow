from django.urls import path

from .views import HomePageView, SearchFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search', SearchFormView.as_view(), name='search')
]
