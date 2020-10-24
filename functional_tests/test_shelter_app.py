import time

from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver

from shelter.models import Animal


class TestShelterAppPages(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

        Animal.objects.create(
            name='Rower',
            age='2',
            gender='male',
            size='small',
            species='cat',
            photo='animal_photos/TEOS.jpeg'
        )

    def tearDown(self):
        self.browser.close()

    def test_animals_cards_display(self):
        self.browser.get(self.live_server_url + reverse('animal-list'))

        card = self.browser.find_element_by_class_name('card')

        self.assertTrue(card)

    def test_animal_list_link_redirects_to_animal_detail(self):
        self.browser.get(self.live_server_url + reverse('animal-list'))

        animal_detail = self.live_server_url + reverse('animal-detail', args=['rower'])
        # causes ConnectionResetError, reason is unknown but test is working right
        self.browser.find_element_by_class_name('animal-card-link').click()

        self.assertEquals(self.browser.current_url, animal_detail)

