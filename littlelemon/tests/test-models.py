from django.test import TestCase
from restaurant.models import Menu


class MenuModelTest(TestCase):
    def create_test_menu(self):
        item = Menu.objects.create(
            name='Breakfast', price=20, description='A selection of breakfast items')
        self.assertEqual(
            str(item), 'Breakfast : A selection of breakfast items')
        self.assertEqual(item.name, 'Breakfast')
        self.assertEqual(item.price, 20)
        self.assertEqual(item.description, 'A selection of breakfast items')
        self.assertEqual(item.calculate_total_cost(), 30)
