from .models import Animal, PetOwner, AnimalGallery
from django.contrib import admin

@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    pass


class AnimalGalleryAdmin(admin.TabularInline):
    model = AnimalGallery

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalGalleryAdmin, ]

    class Meta:
        model=Animal


# @admin.register(AnimalGallery)
# class AnimalGalleryAdmin(admin.ModelAdmin):
#     pass

