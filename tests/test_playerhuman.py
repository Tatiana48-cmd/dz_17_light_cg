import unittest
from unittest.mock import patch
from main import PlayerHuman

class TestPlayerHuman(unittest.TestCase):
    def setUp(self):
        self.player = PlayerHuman("Test Human Player")

    def test_take_turn(self):
        # Выбираем два разных числа из карточки
        number_to_mark_y = self.player.cart.numbers[0]  # Первое число для ввода 'y'
        number_to_mark_n = self.player.cart.numbers[1]  # Второе число для ввода 'n'

        # Симулируем ввод 'y' (зачеркнуть число)
        with patch('builtins.input', return_value='y'):
            self.assertTrue(self.player.take_turn(number_to_mark_y))

        # Симулируем ввод 'n' (не зачеркивать число)
        with patch('builtins.input', return_value='n'):
            self.assertFalse(self.player.take_turn(number_to_mark_n))

if __name__ == "__main__":
    unittest.main()