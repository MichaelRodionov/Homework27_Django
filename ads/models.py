from django.db.models import Model, IntegerField, CharField, BooleanField
from django.forms import SlugField


# ----------------------------------------------------------------
# models
class Advertisement(Model):
    slug = SlugField(max_length=50)
    name = CharField(max_length=400)
    author = CharField(max_length=30)
    price = IntegerField()
    description = CharField(max_length=1000)
    address = CharField(max_length=500)
    is_published = BooleanField()

    def __str__(self):
        return self.slug


class Category(Model):
    slug = SlugField(max_length=50)
    name = CharField(max_length=100)

    def __str__(self):
        return self.slug
