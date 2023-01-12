from django.test import TestCase, SimpleTestCase
from sport_equipment.models import Category, Equipment, Product
from mixer.backend.django import mixer

# mixer и factory boy


class TestCategory(TestCase):

    def setUp(self):
        # self.category = Category.objects.create(name='test category name')
        self.category = mixer.blend(Category)
        print('Я выполняюсь перед каждым тестом')

    def tearDown(self):
        print('Я выполняюсь после каждого теста')
    def test_str(self):
        # category = Category.objects.create(name='test category name')
        print('CATEGORY_NAME', self.category.name)
        self.assertEqual(str(self.category), self.category.name)

    def test_has_equipment_false(self):
        # category = Category.objects.create(name='test category name')
        self.assertFalse(self.category.has_equipment)

    def test_has_equipment_true(self):
        # category = Category.objects.create(name='test category name')
        Equipment.objects.create(category=self.category)
        self.assertTrue(self.category.has_equipment)
#
#
class TestEquipment(TestCase):

    def test_str(self):
        # category = Category.objects.create(name='test category name')
        # equipment = Equipment.objects.create(name='test equipment', category=category)
        equipment = mixer.blend(Equipment, name='test equipment')
        self.assertEqual(str(equipment), 'test equipment')

    def test_get_category_name_title(self):
        equipment = mixer.blend(Equipment, category__name='some name')
        self.assertEqual(equipment.get_category_name_title(), 'SOME NAME')

class TestProduct(SimpleTestCase):

    def test_buy(self):
        # При вызове метода buy мы дожны получить ошибку ?
        product = Product(cost=100, name='Экскурсия')
        with self.assertRaises(NotImplementedError):
            product.buy()

        # try:
        #     product.buy()
        # except NotImplementedError:
        #     pass
        # except Exception as e:
        #     assert False, f'Мы ждали NotImplementedError, возникла {e}'
        # else:
        #     assert False, 'Ошибка не возникла'