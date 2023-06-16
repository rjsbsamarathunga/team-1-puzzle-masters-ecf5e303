from unittest import TestCase
from levelup.character import Character
from levelup.position import Position
from levelup.direction import Direction
from levelup.exceptions import InvalidMoveException
class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
 
    def test_current_position(self):
        x=0
        y=0
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        testobj.enter_map()
        position = testobj.get_position()
        self.assertEqual(x, position.x)
        self.assertEqual(y, position.y)
        
    def test_move_north(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        current_move_count = testobj.get_num_moves()

        # test position
        current_position = Position(3,4)
        testobj.set_position(current_position)
        direction = Direction("n")
        expected_position = Position(3,5)
        testobj.move(direction)
        updated_position = testobj.get_position()
        self.assertTrue(updated_position == expected_position)

        # test move count
        expected_move_count = current_move_count+1
        new_move_count = testobj.get_num_moves()
        self.assertEqual(expected_move_count, new_move_count)

    
    def test_move_south(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        current_move_count = testobj.get_num_moves()

        # test position
        current_position = Position(3,4)
        testobj.set_position(current_position)
        direction = Direction("s")
        expected_position = Position(3,3)
        testobj.move(direction)
        updated_position = testobj.get_position()
        self.assertTrue(updated_position == expected_position)

        # test move count
        expected_move_count = current_move_count+1
        new_move_count = testobj.get_num_moves()
        self.assertEqual(expected_move_count, new_move_count)

    def test_move_east(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        current_move_count = testobj.get_num_moves()

        # test position
        current_position = Position(3,4)
        testobj.set_position(current_position)
        direction = Direction("e")
        expected_position = Position(4,4)
        testobj.move(direction)
        updated_position = testobj.get_position()
        self.assertTrue(updated_position == expected_position)

        # test move count
        expected_move_count = current_move_count+1
        new_move_count = testobj.get_num_moves()
        self.assertEqual(expected_move_count, new_move_count)

    def test_move_west(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        current_move_count = testobj.get_num_moves()

        # test position
        current_position = Position(3,4)
        testobj.set_position(current_position)
        direction = Direction("w")
        expected_position = Position(2,4)
        testobj.move(direction)
        updated_position = testobj.get_position()
        self.assertTrue(updated_position == expected_position)

        # test move count
        expected_move_count = current_move_count+1
        new_move_count = testobj.get_num_moves()
        self.assertEqual(expected_move_count, new_move_count)    
  

    def test_move_west_atWestBoundary(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        current_move_count = testobj.get_num_moves()

        # test position
        current_position = Position(0,4)
        testobj.set_position(current_position)
        direction = Direction("w")
        expected_position = current_position
        testobj.move(direction)
        updated_position = testobj.get_position()
        self.assertTrue(updated_position == expected_position)

        # test move count
        expected_move_count = current_move_count+1
        new_move_count = testobj.get_num_moves()
        self.assertEqual(expected_move_count, new_move_count)    
  