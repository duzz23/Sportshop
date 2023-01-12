from django.core.management.base import BaseCommand
from faker import Faker
from sport_equipment.models import Category, Equipment
from mixer.backend.django import mixer

class Command(BaseCommand):
    help = 'Mixer examples'

    def handle(self, *args, **options):
        print('Generaet data')
        Equipment.objects.all().delete()
        Category.objects.all().delete()
        category = mixer.blend(Category)
        equipment = mixer.blend(Equipment)

        equipment = mixer.blend(Equipment, name='Our name')
        print(equipment.name)

        # 1.
        category = mixer.blend(Category, name='Our name')
        equipment = mixer.blend(Equipment, category=category)

        # 2.
        equipment = mixer.blend(Equipment, category__name='Other name')
        print(equipment.category.name)

        # clients = mixer.cycle(4).blend(Client, username=(name for name in ('Piter', 'John')))
        # categories = mixer.cycle(3).blend(Category)
        # print(categories)

        categories = mixer.cycle(2).blend(Category, name=(name for name in ('Плавание', 'Тенис')))
        print(categories)

        # clients = mixer.cycle(4).blend(Client, username=mixer.sequence(lambda c: "test_%s" % c))

        # categories = mixer.cycle(2).blend(Category, name=mixer.sequence(lambda c: "test_%s" % c))
        # print(categories)

        # clients = mixer.cycle(4).blend(Client, username=mixer.sequence("test_{0}"))

        categories = mixer.cycle(2).blend(Category, name=mixer.sequence("test_{0}"))
        print(categories)

        # client = mixer.blend(Client, score=mixer.RANDOM)
        category = mixer.blend(Category, rating=mixer.RANDOM)
        print(category.rating)

        # message = mixer.blend(Message, client=mixer.SELECT)
        equipment = mixer.blend(Equipment, category=mixer.SELECT)

        print(equipment.category)

        print('done')


