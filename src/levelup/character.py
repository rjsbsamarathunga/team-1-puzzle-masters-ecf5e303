from levelup.position import Position
from levelup.direction import Direction
from levelup.gamemap import GameMap
class Character:
    name = ""
    
    def __init__(self, character_name):
        self.name = character_name
        self.position = Position(GameMap.x_starting_position, GameMap.y_starting_position)
        self.num_move = 0

    def move(self, direction: Direction) -> None:      
        self.num_move +=1
        self.position = GameMap.calculate_position(self.position, direction)

    def get_position(self):
        return self.position

    #def get_num_moves():
