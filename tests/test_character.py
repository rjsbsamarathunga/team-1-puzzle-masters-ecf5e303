from unittest import TestCase
from levelup.character import Character

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
        position = testobj.get_position()
        self.assertEqual(x, position.x)
        self.assertEqual(y, position.y)
        
    

