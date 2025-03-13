import unittest
import random
from main import Player
from main import Cart

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "Test Player")
        self.assertIsInstance(self.player.cart, Cart)

    def test_player_str(self):
        self.assertIn("Test Player", str(self.player))