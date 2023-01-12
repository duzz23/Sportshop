from django.core.management.base import BaseCommand
from faker import Faker
from sport_equipment.models import Category, Equipment

class Command(BaseCommand):
    help = 'Faker examples'

    def handle(self, *args, **options):
        print('Generaet data')

        fake = Faker()

        print(fake.name())
        # 'Lucy Cechtelar'

        print(fake.address())
        # '426 Jordy Lodge
        #  Cartwrightshire, SC 88120-6700'

        print(fake.text())

        fake = Faker(['ru_RU'])
        for _ in range(10):
            print(fake.name())


        category = Category.objects.create(name=fake.name())
        print(category.name)

        print(fake.first_name())

        fake = Faker(['ar_AA'])

        print(fake.first_name())

        category = Category.objects.create(name=fake.name())

        print(fake.pydict())