from django.db.models import Model, IntegerField, CharField, BooleanField


# ----------------------------------------------------------------
# models
class Advertisement(Model):
    name = CharField(max_length=300)
    author = CharField(max_length=30)
    price = IntegerField()
    description = CharField(max_length=1000)
    address = CharField(max_length=500)
    is_published = BooleanField()


class Category(Model):
    name = CharField(max_length=100)
