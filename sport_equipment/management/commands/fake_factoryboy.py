from django.core.management.base import BaseCommand
from sport_equipment.factories import CategoryFactory, EquipmentFactory
from sport_equipment.models import Category, Equipment
from factory import django

class Command(BaseCommand):
    help = 'Factory Boy examples'

    def handle(self, *args, **options):
        print('Test data is generating')
        Category.objects.all().delete()
        Equipment.objects.all().delete()

        print('-'*100)
        category = CategoryFactory(name='Теннис')
        print(category.name)
        print(category.id)
        print(category.is_active)

        print('-' * 100)
        category = CategoryFactory.build()
        print(category.name)
        print(category.id)
        print(category.is_active)

        print('-' * 100)
        category = CategoryFactory.create(name='Зимние виды спорта')
        print(category.name)
        print(category.id)
        print(category.is_active)

        print('-' * 100)
        equipment = EquipmentFactory.create()
        print(equipment.name)
        print(equipment.category.name)
        print(equipment.category.id)
        print(equipment.category.is_active)
        print(equipment.id)

        equipments = EquipmentFactory.build_batch(10)
        print(equipments)