from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction
class TestGameMap(TestCase):
    def test_is_position_valid(self):
        x = 0
        y = 9
        position = Position(x,y)
        self.assertTrue(position.x < 10)
        self.assertTrue(position.y < 10)
        self.assertTrue(position.x >= 0)
        self.assertTrue(position.y >= 0)

    def test_is_position_valid_xyinrange_true(self):
        x = 0
        y = 9
        position = Position(x,y)
        self.assertTrue(GameMap.is_position_valid(position))

    def test_is_position_valid_lessthanxstart_false(self):
        x = -1
        y = 0
        position = Position(x,y)
        self.assertFalse(GameMap.is_position_valid(position))

    def test_is_position_valid_greaterthanxend_false(self):
        x = -11
        y = 0
        position = Position(x,y)
        self.assertFalse(GameMap.is_position_valid(position))

    # TODO: ^ y

    def test_calculate_position_n(self):
        direction = Direction("n")
        current_position = Position(5,6)
        expected_position = Position(5,7)
        new_position = GameMap.calculate_position(current_position, direction)
        self.assertTrue(new_position == expected_position)

    # TODO: ^ for s, e, w, invalid

    def test_total_positions(self):
        total_positions=100
        self.assertEqual(total_positions, GameMap.get_total_positions())
        