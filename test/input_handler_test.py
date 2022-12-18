import unittest.mock
from typing import Callable

import pytest

from src.input import Input
from src.input_handler import InputHandler


@pytest.mark.parametrize(
    "input",
    [
        Input.MOVE_RIGHT,
        Input.MOVE_LEFT,
        Input.DROP,
        Input.ROTATE_CLOCKWISE,
        Input.ROTATE_ANTI_CLOCKWISE,
        Input.QUIT
    ]
)
def test_handle_given_known_input_invokes_expected_callable(input: Input) -> None:
    # Arrange.
    input_handler = InputHandler()

    move_right = unittest.mock.create_autospec(Callable[[], None])
    move_left = unittest.mock.create_autospec(Callable[[], None])
    drop = unittest.mock.create_autospec(Callable[[], None])
    rotate_clockwise = unittest.mock.create_autospec(Callable[[], None])
    rotate_anti_clockwise = unittest.mock.create_autospec(Callable[[], None])
    quit = unittest.mock.create_autospec(Callable[[], None])
    input_handler.initialise(move_right, move_left, drop, rotate_clockwise, rotate_anti_clockwise, quit)

    # Act.
    input_handler.handle(input)

    # Assert.
    input_to_expected_called_callable = {
        Input.MOVE_RIGHT: move_right,
        Input.MOVE_LEFT: move_left,
        Input.DROP: drop,
        Input.ROTATE_CLOCKWISE: rotate_clockwise,
        Input.ROTATE_ANTI_CLOCKWISE: rotate_anti_clockwise,
        Input.QUIT: quit
    }
    input_to_expected_called_callable[input].assert_called_once()


def test_handle_raises_value_error_given_invalid_input():
    # Arrange.
    input_handler = InputHandler()

    mock_callable = unittest.mock.create_autospec(Callable[[], None])
    input_handler.initialise(mock_callable, mock_callable, mock_callable, mock_callable, mock_callable, mock_callable)

    # Act & Assert.
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        input_handler.handle(-1)
