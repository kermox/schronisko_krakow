from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (Animal, AnimalGallery, PetOwner, ShelterGallery,
                     ShelterGalleryPhotos)


@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_animals']
    search_fields = ['first_name', 'second_name', 'email', 'phone_number']

    def get_animals(self, instance):
        return [i.name.upper() for i in instance.animal_set.all()]
    get_animals.short_description = 'adaptowane zwierzęta'


class AnimalGalleryAdmin(admin.TabularInline):
    """
    Makes possible to do CRUD operations on related model change page.
    (No need to register as a separate admin model)
    """
    model = AnimalGallery


class AnimalAgeFilter(admin.SimpleListFilter):
    title = _('przybliżony wiek')
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            ('<1', '0-1'),
            ('1-3', '1-3'),
            ('3-5', '3-5'),
            ('5+', '5+'),
        )

    def queryset(self, request, queryset):
        if self.value() == '<1':
            return queryset.filter(age__lte=1)
        if self.value() == '1-3':
            return queryset.filter(age__range=[1, 3])
        if self.value() == '3-5':
            return queryset.filter(age__range=[3, 5])
        if self.value() == '5+':
            return queryset.filter(age__gte=5)



@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalGalleryAdmin, ]
    fieldsets = (
        (None, {
            'fields': ['name', 'age', 'gender', 'size', 'species', 'other_species', 'breed', 'coat',
                       'additional_information', 'photo', ]
        }),
        ('Szczegółowe informacje', {
            'classes': ('collapse',),
            'fields': ('find_place', 'date_of_registration', 'adopted','adopted_by', 'date_of_adoption', 'chip_number',
                       'identification_number', 'medical_information', 'documents', ),
        }),
    )
    list_display = ['__str__', 'adopted']
    search_fields = ['name', 'additional_information', 'identification_number', 'chip_number', 'adopted_by__first_name', ]
    list_filter = [AnimalAgeFilter, 'adopted', 'size', ]
    date_hierarchy = 'created_at'


class ShelterGalleryPhotosAdmin(admin.TabularInline):
    """
    Makes possible to do CRUD operations on related model change page.
    (No need to register as a separate admin model)
    """
    model = ShelterGalleryPhotos


@admin.register(ShelterGallery)
class ShelterGalleryAdmin(admin.ModelAdmin):
    inlines = [ShelterGalleryPhotosAdmin, ]
    readonly_fields = ['gallery_name', ]

    def has_add_permission(self, request):
        has_permission = super(ShelterGalleryAdmin, self).has_add_permission(request)

        # Check for the user permission and object instance.
        if has_permission and ShelterGallery.objects.exists():
            # If user has permission and there is already an instance in database,
            # set the permission to False
            has_permission = False
        return has_permission
