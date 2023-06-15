from levelup.position import Position
from levelup.direction import Direction
class GameMap:
    x_start=0
    x_end=9
    y_start=0
    y_end=9
    num_positions=100
    x_starting_position=0
    y_starting_position=0

    def calculate_position(starting_position: Position, direction: Direction) -> Position:
        new_position = Position(starting_position.x, starting_position.y)
        if direction.EAST:
            new_position.x += 1 
        if direction.WEST:
            new_position.x -= 1
        if direction.NORTH:
            new_position.y += 1
        if direction.SOUTH:
            new_position.y -= 1
        if is_position_valid(new_position):
            return new_position
        else:
            return starting_position 


        
            

    def is_position_valid(postion: Position) -> bool:
        if postion.x not in range(GameMap.x_start, GameMap.x_end+1):
            return False
        if postion.y not in range(GameMap.y_start, GameMap.y_end+1):
            return False
        return True

    def get_total_positions() -> int:
        return GameMap.num_positions

