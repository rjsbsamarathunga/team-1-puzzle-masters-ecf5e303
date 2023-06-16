from levelup.position import Position
from levelup.direction import Direction
from levelup.gamemap import GameMap
from levelup.exceptions import InvalidMoveException
class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name
        self.num_move = 0

    def move(self, direction: Direction) -> None:      
        self.num_move +=1
        self.current_position = GameMap.calculate_position(self.current_position, direction)

    def get_position(self) -> Position:
        return self.current_position

    def set_position(self,position) -> Position:
        self.current_position = position

    def get_num_moves(self) -> int:
        return self.num_move

    def enter_map(self):
        self.current_position = Position(GameMap.x_character_starting, GameMap.y_character_starting)