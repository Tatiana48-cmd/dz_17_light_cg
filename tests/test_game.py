import unittest
from main import Player
from main import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_initialization(self):
        self.assertEqual(len(self.game.barrels), 90)
        self.assertIsInstance(self.game.player1, Player)
        self.assertIsInstance(self.game.player2, Player)

    def test_game_str(self):
        self.assertIn("Игра между", str(self.game))

    def test_game_eq(self):
        game2 = Game()
        self.assertFalse(self.game == game2)

if __name__ == "__main__":
    unittest.main()