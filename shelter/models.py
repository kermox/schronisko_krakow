from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from utils.utils import get_image_name, unique_slug_generator, TimeStampMixin


class PetOwner(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='imię',
    )
    second_name = models.CharField(
        max_length=50,
        verbose_name='nazwisko',
    )
    address = models.CharField(
        max_length=150,
        verbose_name='adress',
        help_text='Podaj adress zamieszkania',
    )
    email = models.EmailField(
        verbose_name='e-mail',
    )
    phone_number = models.PositiveIntegerField(
        verbose_name='numer telefonu'
    )
    adopting_agreement = models.FileField(
        upload_to='agreements/',
        verbose_name='umowa adopcyjna',
    )

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.email}'


class Animal(TimeStampMixin, models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='imię',
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, 'Wiek nie może być <= 0'),
            MaxValueValidator(40, 'Wiek nie może być większy od 30')
        ],
        verbose_name='przybliżony wiek',
        help_text='Wprowadź przybliżony wiek'
    )

    slug = models.SlugField(
        max_length=250,
        blank=True,
        null=True,
    )

    SPECIES_CHOICES = [
        ('dog', 'Pies'),
        ('cat', 'Kot'),
        ('other', 'Inny')
    ]
    species = models.CharField(
        max_length=50,
        verbose_name='gatunek',
        choices=SPECIES_CHOICES,
    )
    other_species = models.CharField(
        max_length=50,
        blank=True,
        null=False,
        default='',
        verbose_name='inny gatunek',
        help_text='Wprowadź gatunek',
    )
    breed = models.CharField(
        max_length=50,
        blank=True,
        null=False,
        default='',
        verbose_name='rasa',
    )
    GENDER_CHOICES = [
        ('male', 'Samiec'),
        ('female', 'Samica'),
    ]
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        verbose_name='płeć',
    )
    SIZE_CHOICES = [
        ('small', 'Mały'),
        ('medium', 'Średni'),
        ('big', 'Duży'),
    ]
    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        verbose_name='wielkość',
        help_text='Wielkość zwierzęcia',
    )
    coat = models.CharField(
        max_length=20,
        blank=True,
        null=False,
        default='',
        verbose_name='umaszczenie',
        help_text='Określ umaszczenie zwierza',
    )
    find_place = models.CharField(
        max_length=128,
        blank=True,
        default='',
        verbose_name='Miejsce gdzie znaleziono zwierzę',
    )
    date_of_registration = models.DateField(
        verbose_name='Data rejestracji',
        blank=True,
        null=True,
    )
    date_of_adoption = models.DateField(
        verbose_name='Data adopcji',
        blank=True,
        null=True,
    )
    chip_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='numer chip',
    )
    identification_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='identyfikator',
    )
    medical_information = models.TextField(
        blank=True,
        default='',
        verbose_name='Stan zdrowia',
    )
    documents = models.FileField(
        upload_to='animal_documents/',
        verbose_name='dokumenty',
        blank=True,
        default='',
    )
    additional_information = models.TextField(
        blank=True,
        default='Ten piesek/kotek jeszcze nie ma opisu. Jedno wiemy napewno - będzie super szczęśliwy w nowej rodzinie',
        verbose_name='dodatkowe informacje',

    )
    photo = models.ImageField(
        upload_to=get_image_name,
        verbose_name='zdjęcie',
    )
    adopted = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name='adaptowany'
    )
    adopted_by = models.ForeignKey(
        PetOwner,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        if not self.adopted:
            return f'{self.name.upper()} - {self.get_species_display()} - Wiek: {self.age}'
        else:
            return f'{self.name.upper()} - Zaadaptowany przez: {self.adopted_by}'

    def get_absolute_url(self):
        return reverse('animal-detail', kwargs={"slug": self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if instance.adopted_by:
        instance.adopted = True


pre_save.connect(pre_save_receiver, sender=Animal)


class AnimalGallery(models.Model):
    animal = models.ForeignKey(Animal, related_name='photos', default=None, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to=get_image_name,
                               verbose_name='zdjęcia')

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galeria"


class ShelterGallery(models.Model):
    gallery_name = models.CharField(
        max_length=200,
        default='Galeria zdjęć',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Galeria zdjęć'
        verbose_name_plural = 'Galeria zdjęć'

    def __str__(self):
        return self.gallery_name


class ShelterGalleryPhotos(models.Model):
    gallery_name = models.ForeignKey(ShelterGallery, related_name='photos', default=None, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='gallery_photos',
        blank=True,
        null=False,
    )
