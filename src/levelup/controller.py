import logging
from dataclasses import dataclass
from levelup.direction import Direction
from levelup.character import Character
from levelup.gamemap import GameMap

DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0


class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()
        self.character = None

    def start_game(self):
        self.character.enter_map()
        current_position = self.character.get_position()
        self.status.current_position = (current_position.x, current_position.y)
        self.status.running = True

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
            self.character = Character(character_name)
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME
            self.character = Character(DEFAULT_CHARACTER_NAME)

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        self.character.move(direction)
        current_position = self.character.get_position()
        self.status.current_position = (current_position.x, current_position.y)
        self.status.move_count = self.character.get_num_moves()

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        self.character.set_position(xycoordinates([0]), xycoordinates([1]))

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        self.status.move_count = self.character.get_num_moves()

    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return GameMap.get_total_positions()

    
