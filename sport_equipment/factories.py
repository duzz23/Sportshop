import factory
from factory import django
from .models import Category, Equipment


class CategoryFactory(django.DjangoModelFactory):

    name = 'Плавание'
    is_active = factory.Iterator([True, False, False, True])

    class Meta:
        model = Category


class EquipmentFactory(django.DjangoModelFactory):

    # name = factory.Faker('name')
    name = factory.Faker('address')
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Equipment