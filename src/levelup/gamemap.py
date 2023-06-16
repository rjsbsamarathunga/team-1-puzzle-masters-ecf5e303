from levelup.position import Position
from levelup.direction import Direction
from levelup.exceptions import InvalidMoveException
class GameMap:
    x_start=0
    x_end=9
    y_start=0
    y_end=9
    num_positions=100
    x_character_starting=0
    y_character_starting=0

    def calculate_position(starting_position: Position, direction: Direction) -> Position:
        new_position = Position(starting_position.x, starting_position.y)
        if direction == Direction.EAST:
            new_position.x += 1 
        if direction == Direction.WEST:
            new_position.x -= 1
        if direction == Direction.NORTH:
            new_position.y += 1
        if direction == Direction.SOUTH:
            new_position.y -= 1
        if GameMap.is_position_valid(new_position):
            return new_position
        return starting_position 

    def is_position_valid(postion: Position) -> bool:
        if postion.x not in range(GameMap.x_start, GameMap.x_end+1):
            # raise InvalidMoveException
            return False
        if postion.y not in range(GameMap.y_start, GameMap.y_end+1):
            # raise InvalidMoveException
            return False
        return True

    def get_total_positions() -> int:
        return GameMap.num_positions