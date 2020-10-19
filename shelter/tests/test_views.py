from django.test import TestCase, Client
from django.urls import reverse
from shelter.models import Animal
from mails.models import EmailAddress


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.animal_list_url = reverse('animal-list')
        self.home_page_url = reverse('home')
        self.animal_detail_url = reverse('animal-detail', args=['rower'])

        Animal.objects.create(
            name='Rower',
            age='2',
            gender='male',
            size='small',
            species='cat',
            photo='animal_photos/TEOS.jpeg'
        )

    def test_animal_list_GET(self):

        response = self.client.get(self.animal_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shelter/animal-list.html')

    def test_home_page_GET(self):

        response = self.client.get(self.home_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shelter/home.html')

    def test_animal_detail_GET(self):

        response = self.client.get(self.animal_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shelter/animal-detail.html')

    def test_animal_detail_POST(self):

        response = self.client.post(self.animal_detail_url, {
            'address': 'example@gmail.com'
        })

        self.assertEquals(response.status_code, 302)
        # POST request is dealing with EmailAddress model
        self.assertEquals(EmailAddress.objects.first().address, 'example@gmail.com')
