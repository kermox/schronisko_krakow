import string
import random
from django.utils.text import slugify
from django.db import models


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
