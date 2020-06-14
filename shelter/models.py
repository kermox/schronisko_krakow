from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Animal(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name='imię',
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, 'Wiek nie może być <= 0'),
            MaxValueValidator(40, 'Wiek nie może być większy od 30')
        ],
        verbose_name='wiek',
        help_text='Wprowadź przybliżony wiek'
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
    date_of_adoption = models.DateField(
        verbose_name='Data adopcji',
        blank=True,
        default='',
    )
    chip_number = models.PositiveIntegerField(
        blank=True,
        default='',
        verbose_name='numer chip',
    )
    identification_number = models.PositiveIntegerField(
        blank=True,
        default='',
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
    additional_information = models.CharField(
        max_length=250,
        blank=True,
        default='',
        verbose_name='dodatkowe informacje',

    )
    photo = models.ImageField(
        upload_to='animal_photos/',
        verbose_name='zdjęcie',
    )


class PetOwner(models.Model):

    first_name = models.CharField(
        max_length=50,
        verbose_name='imię',
    )
    second_name = models.CharField(
        max_length=50,
        verbose_name='nazwisko',
    )
    adress = models.CharField(
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
    animal = models.ForeignKey(
        Animal,
        on_delete=models.PROTECT,
        verbose_name='adoptowane zwiere',
        help_text='Wybierz zwierzę które chcesz zaadaptować',
    )
    adopting_agreement = models.FileField(
        upload_to='agreements/',
        verbose_name='umowa adopcyjna',
    )
