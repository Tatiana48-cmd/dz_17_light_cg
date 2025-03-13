import unittest
from main import PlayerComp


class TestPlayerComp(unittest.TestCase):
    def setUp(self):
        self.player = PlayerComp("Test Comp Player")

    def test_take_turn(self):
        number_to_mark = self.player.cart.numbers[0]
        self.assertTrue(self.player.take_turn(number_to_mark))