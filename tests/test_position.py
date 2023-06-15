import unittest 
from levelup.position import Position

class TestPosition(unittest.TestCase):
    def test_init(self):
        x = 1
        y = 5
        testobj = Position(x, y)
        self.assertEqual(x, testobj.x)
        self.assertEqual(y, testobj.y)

unittest.main()