import random

from .priority_queue import PriorityQueue
from .utils import Coordinate

class SquareGrid:
    def __init__(self, rows, cols, start, target, empty_space_chance: float = 0.8, seed=42):
        self.grid = None
        self.start = None
        self.create_square_grid(rows, cols, empty_space_chance, seed)
        self.place_start_and_target(start, target)

    def create_square_grid(self, rows: int, cols: int, empty_space_chance: float, seed: int) -> None:
        random.seed(seed)
        self.grid = [[0 if random.uniform(0, 1) < empty_space_chance else 1 for _ in range(cols)] for _ in range(rows)]

    def place_start_and_target(self, start: tuple[int, int], target: tuple[int, int]) -> None:
        self.grid[start[0]][start[1]] = 2
        self.start = Coordinate(start[0], start[1], 0)

        self.grid[target[0]][target[1]] = 3

    def astar(self):
        open_pq = PriorityQueue([self.start])
        closed = set()

        while True:
            current = open_pq.get_root_value()
            open_pq.remove()
            closed.add(current)
            if self.grid[current.x][current.y] == 4:
                return

    def _get_neighbors(self, x: int, y: int) -> list[Coordinate]:
        # for i in range(-1, 2):
        #     for j in range(-1, 2):
        #         if i == 0 and j == 0:
        #             continue
        #
        #         if x + i >= 0 and x + i < len(self.grid[0]) and y + j >= 0 and y + j < len(self.grid):
        #             coordinate = Coordinate(x + i, y + j, )
        pass

    def _euclidean_distance(self, start_x, start_y, target_x, target_y) -> int:
        return 14 * min(abs(start_x - target_x), abs(start_y - target_y)) + 10 * abs(abs(start_x - target_x) - abs(start_y - target_y))

    def __repr__(self):
        return "".join(f"{row}\n" for row in self.grid)

sg = SquareGrid(5, 10, (0, 0), (4, 9), empty_space_chance=0.65)
