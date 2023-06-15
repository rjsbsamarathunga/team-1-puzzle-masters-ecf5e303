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




