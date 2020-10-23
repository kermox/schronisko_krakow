from django.test import SimpleTestCase

from shelter.forms import SearchAnimalForm


class TestForms(SimpleTestCase):

    def test_search_animal_form_is_valid(self):
        form = SearchAnimalForm(data={
            'species': 'cat',
            'name': 'skaza',
            'size': 'big',
            'age': 3,
            'gender': 'male',
            'chip_number': 2304982903,
            'identification_number': 230420,
        })

        self.assertTrue(form.is_valid())

    def test_search_animal_form_no_data(self):
        form = SearchAnimalForm(data={})

        self.assertTrue(form.is_valid())