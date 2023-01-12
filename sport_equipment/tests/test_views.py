from django.test import TestCase, Client

from sport_equipment.models import Category


class TestEquipmentList(TestCase):

    # def setUp(self):
    #     self.client = Client()

    def test_response_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        response = self.client.get('/')
        self.assertIn('<h1>Equipments</h1>'.encode(encoding='utf-8'), response.content)
        self.assertIn('<h1>Equipments</h1>', response.content.decode(encoding='utf-8'))


class TestCategoryList(TestCase):

    def test_category_in_list(self):
        response = self.client.get('/category/list/')
        self.assertNotIn('ABCDEF'.encode(encoding='utf-8'), response.content)
        Category.objects.create(name='ABCDEF')
        response = self.client.get('/category/list/')
        self.assertIn('ABCDEF'.encode(encoding='utf-8'), response.content)

    def test_category_in_context(self):
        category = Category.objects.create(name='ABCDEF')
        response = self.client.get('/category/list/')
        context = response.context
        # print(type(context))
        # for item in context:
        #     print(type(item))
        #     print(item)
        self.assertIn('categories', context)
        self.assertIn(category, context['categories'])