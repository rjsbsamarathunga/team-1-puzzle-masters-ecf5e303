from unittest import TestCase
from levelup.controller import GameController

class TestGameControllerInit(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
        assert testObj.character == None

class TestGameControllerStartGame(TestCase):
    def test_init(self):
        testObj = GameController()
        testObj.create_character("Test") 
        testObj.start_game()
