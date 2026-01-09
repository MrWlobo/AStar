import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.square_grid_astar import SquareGrid

@pytest.fixture
def square_grid():
    sg = SquareGrid(10, 10, (1, 1), (9, 9))
    return sg

@pytest.mark.parametrize("x_start, y_start, x_target, y_target, expected", [
    (0, 0, 0, 0, 0),
    (0, 0, 2, 2, 28),
    (3, 2, 8, 9, 90)
])
def test__euclidean_distance(square_grid, x_start, y_start, x_target, y_target, expected):
    assert square_grid._euclidean_distance(x_start, y_start, x_target, y_target) == expected