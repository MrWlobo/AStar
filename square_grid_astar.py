import random


class SquareGrid:
    def __init__(self, rows, cols, start, target, empty_space_chance: float = 0.8, seed=42):
        self.grid = None
        self.create_square_grid(rows, cols, empty_space_chance, seed)
        self.place_start_and_target(start, target)

    def create_square_grid(self, rows: int, cols: int, empty_space_chance: float, seed: int) -> None:
        random.seed(seed)
        self.grid = [[0 if random.uniform(0, 1) < empty_space_chance else 1 for _ in range(cols)] for _ in range(rows)]

    def place_start_and_target(self, start: tuple[int, int], target: tuple[int, int]) -> None:
        self.grid[start[0]][start[1]] = 2
        self.grid[target[0]][target[1]] = 3

    def __repr__(self):
        return "".join(f"{row}\n" for row in self.grid)

sg = SquareGrid(5, 10, (0, 0), (4, 9), empty_space_chance=0.65)
