from .models import Animal, PetOwner
from django.contrib import admin


class AnimalAdmin(admin.ModelAdmin):
    pass


class PetOwnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Animal, AnimalAdmin)
admin.site.register(PetOwner, PetOwnerAdmin)
