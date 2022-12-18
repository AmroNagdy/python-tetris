from typing import List

import pytest

from abstract_tetromino import Tetromino
from grid_offset import GridOffset
from input import Input


class TestTetromino(Tetromino):
    rotation_0 = [GridOffset(0, 0)]
    rotation_1 = [GridOffset(1, 1)]
    rotation_2 = [GridOffset(2, 2)]
    rotation_3 = [GridOffset(3, 3)]

    def __init__(self):
        super().__init__(
            TestTetromino.rotation_0,
            TestTetromino.rotation_1,
            TestTetromino.rotation_2,
            TestTetromino.rotation_3
        )


@pytest.mark.parametrize(
    "clockwise_rotations,expected_rotation",
    [
        (0, TestTetromino.rotation_0),
        (1, TestTetromino.rotation_1),
        (2, TestTetromino.rotation_2),
        (3, TestTetromino.rotation_3),
        (4, TestTetromino.rotation_0),
        (5, TestTetromino.rotation_1),
    ]
)
def test_clockwise_rotations_set_expected_rotation_state(
        clockwise_rotations: int,
        expected_rotation: List[GridOffset]
) -> None:
    # Arrange.
    tetromino = TestTetromino()

    # Act.
    for _ in range(clockwise_rotations):
        tetromino.rotate(Input.ROTATE_CLOCKWISE)

    # Assert.
    assert tetromino.get_offset() == expected_rotation


@pytest.mark.parametrize(
    "anti_clockwise_rotations,expected_rotation",
    [
        (0, TestTetromino.rotation_0),
        (1, TestTetromino.rotation_3),
        (2, TestTetromino.rotation_2),
        (3, TestTetromino.rotation_1),
        (4, TestTetromino.rotation_0),
        (5, TestTetromino.rotation_3),
    ]
)
def test_clockwise_rotations_set_expected_rotation_state(
        anti_clockwise_rotations: int,
        expected_rotation: List[GridOffset]
) -> None:
    # Arrange.
    tetromino = TestTetromino()

    # Act.
    for _ in range(anti_clockwise_rotations):
        tetromino.rotate(Input.ROTATE_ANTI_CLOCKWISE)

    # Assert.
    assert tetromino.get_offset() == expected_rotation
