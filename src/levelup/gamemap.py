from levelup.position import Position
from levelup.controller import Direction
class GameMap:
    x_start=0
    x_end=9
    y_start=0
    y_end=9
    num_positions=100

    def calculate_position(starting_position: Position, direction: Direction) -> Position:
        pass

    def is_position_valid(postion: Position) -> bool:
        pass

    def get_total_positions() -> int:
        return num_positions

