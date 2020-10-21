from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shelter.views import AnimalListView, AnimalDetail, HomePageView


class TestUrls(SimpleTestCase):

    def test_animal_list_url_resolves(self):
        url = reverse('animal-list')
        self.assertEquals(resolve(url).func.view_class, AnimalListView)

    def test_animal_detail_url_resolves(self):
        url = reverse('animal-detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, AnimalDetail)

    def test_home_page_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePageView)
