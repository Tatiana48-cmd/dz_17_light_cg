import unittest
import random
from main import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_cart_initialization(self):
        self.assertEqual(len(self.cart.numbers), 15)
        self.assertEqual(len(self.cart.rows), 3)
        for row in self.cart.rows:
            self.assertEqual(len(row), 9)
            self.assertEqual(sum(1 for num in row if num != '  '), 5)

    def test_mark_number(self):
        number_to_mark = self.cart.numbers[0]
        self.assertTrue(self.cart.mark_number(number_to_mark))
        self.assertFalse(self.cart.mark_number(100))  # Числа нет на карточке

    def test_is_complete(self):
        for number in self.cart.numbers:
            self.cart.mark_number(number)
        self.assertTrue(self.cart.is_complete())







