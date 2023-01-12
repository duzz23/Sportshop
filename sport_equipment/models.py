from django.db import models
from django.utils.functional import cached_property


class TimestampMixin(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_timestamp(self):
        print(self.create, self.update)

    class Meta:
        abstract = True

class Category(TimestampMixin):
    name = models.CharField(unique=True, max_length=32)
    is_active = models.BooleanField(default=True)
    # 1. Blob (Bites), 2. На диске
    img = models.ImageField(upload_to='category', blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)
    # Сколько товаров в этой категории
    @cached_property
    def equipment_count(self):
        equipments = Equipment.objects.filter(category=self)
        # result = len(equipments)
        result = equipments.count()
        return result

    @cached_property
    def has_equipment(self):
        # result = len(Equipment.objects.filter(category=self)) > 0
        # result = Equipment.objects.filter(category=self).count() > 0
        result = Equipment.objects.filter(category=self).exists()
        return result



    # models.IntegerField
    # models.TextField
    # models.FloatField
    # models.BooleanField
    # models.JSONField
    # models.DecimalField
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # models.EmailField
    # models.URLField
    # models.SlugField
    # models.BinaryField
    # models.ImageField
    # models.TextField
    def __str__(self):
        return self.name


class Product(models.Model):
    # cost = models.DecimalField
    cost = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=64)

    def buy(self):
        raise NotImplementedError()

# Оборудование ЯВЛЯЕТСЯ Товаром ?
class Equipment(Product, TimestampMixin):

    # class Meta:
    #     unique_together = ('name', 'category',)

    # CASCADE, SET_NULL, PROTECTED
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_own_shop = models.BooleanField(default=False)
    def get_category_name_title(self):
        return self.category.name.upper()

    def buy(self):
        print('Купили', self.name)

    def __str__(self):
        return f'{self.name}'


class DebugEquipment(Equipment):

    class Meta:
        proxy = True

    def buy(self):
        print(self.create)
        super().buy()
        print(self.update)


class Excursion(Product, TimestampMixin):
    days_count = models.PositiveIntegerField(default=1)


class ContactSent(models.Model):
    name = models.CharField('Ваше имя', max_length=400)
    date_burn = models.DateTimeField('дата рождения', blank=True, null=True, max_length=50)
    telefon = models.IntegerField('Телефон')
    email = models.EmailField('Почта', unique=True)
    description = models.CharField('Описание', blank=True, null=True, max_length=50)


    def __str__(self):
        return self.name

