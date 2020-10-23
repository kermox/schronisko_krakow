import random
import string

from django.db import models
from django.utils.text import slugify


class TimeStampMixin(models.Model):
    """
    Class to update models with DateTimeFields.
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        if hasattr(instance, 'title'):
            slug = slugify(instance.title)
        else:
            slug = slugify(instance.name)
    InstanceClass = instance.__class__
    qs_exists = InstanceClass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def get_image_name(instance, filename):
    if instance.__class__.__name__ == 'Animal':
        return f'animal_photos/{instance.name}/profile_photo/{filename}'
    elif instance.__class__.__name__ == 'AnimalGallery':
        return f'animal_photos/{instance.animal.name}/gallery/{filename}'
    elif instance.__class__.__name__ == 'ShelterGalleryPhotos':
        return f'shelter_photos/{filename}'
    elif instance.__class__.__name__ == 'SideContent':
        return f'news/{instance.category.name}/{filename}'
    else:
        return 'other_images/'
