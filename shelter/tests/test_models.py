from django.test import TestCase

from shelter.models import Animal, PetOwner


class TestModels(TestCase):

    def setUp(self):

        self.pet_owner = PetOwner.objects.create(
            first_name='Maksym',
            second_name='Garus',
            address='test address',
            email='test@email.com',
            phone_number='12345678',
            adopting_agreement='agreement.pdf'
        )

        self.animal = Animal.objects.create(
            name='Rower',
            age='2',
            gender='male',
            size='small',
            species='cat',
            photo='animal_photos/TEOS.jpeg',
            adopted_by=self.pet_owner
        )

    def test_animal_is_assigned_slug_on_creation(self):
        self.assertEquals(self.animal.slug, 'rower')

    def test_is_animal_adopted_checked_when_adopted_by(self):
        self.assertTrue(self.animal.adopted)
