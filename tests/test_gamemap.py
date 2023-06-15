from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position

class TestGameMap(TestCase):
    def test_is_position_valid(self):
        x = 0
        y = 9
        position = Position(x,y)
        self.assertTrue(position.x < 10)
        self.assertTrue(position.y < 10)
        self.assertTrue(position.x >= 0)
        self.assertTrue(position.y >= 0)


    def test_is_position_pass(self):
        x = 0
        y = 9
        position = Position(x,y)
        self.assertTrue(GameMap.is_position_valid(position))

    def test_is_position_fail(self):
        x = -1
        y = 0
        position = Position(x,y)
        self.assertFalse(GameMap.is_position_valid(position))

    def test_total_positions(self):
        total_positions=100
        self.assertEqual(total_positions, GameMap.get_total_positions())
        