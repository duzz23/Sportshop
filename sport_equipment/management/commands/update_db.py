from django.core.management.base import BaseCommand
from django.db.models import F, Q, Sum, Window
from django.db.models.functions import CumeDist

from sport_equipment.models import Category

class Command(BaseCommand):
    help = 'Bulk update example'

    def handle(self, *args, **options):
        print('start')
        categories = Category.objects.all()
        # for category in categories:
        #     category.is_active = False
        #     category.save()
        categories.update(is_active=False)

        print('Old rating')
        for category in categories:
            print(category.name, '->', category.rating)

        # скриптом увеличить рейтинг у всех на 1
        categories = Category.objects.all()
        # for category in categories:
        #     category.rating += 1
        #     category.save()
        categories.update(rating=F('rating')+1)

        print('New rating')
        for category in categories:
            print(category.name, '->', category.rating)

        # Агрегация
        print('Суммарный рейтинг')
        sum_rating = 0
        for category in categories:
            sum_rating += category.rating
        print(sum_rating)

        print('Суммарный рейтинг агрегация')
        sum_rating = Category.objects.aggregate(Sum('rating'))
        print(sum_rating)
        print(sum_rating['rating__sum'])
        print('end')