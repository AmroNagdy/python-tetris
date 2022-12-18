import curses
import unittest.mock

import pytest

from input import Input
from input_handler import InputHandler
from input_thread import InputThread


@pytest.mark.parametrize(
    "input_ord,expected_input",
    [
        (curses.KEY_RIGHT, Input.MOVE_RIGHT),
        (curses.KEY_LEFT, Input.MOVE_LEFT),
        (curses.KEY_DOWN, Input.DROP),
        (ord("d"), Input.ROTATE_CLOCKWISE),
        (ord("a"), Input.ROTATE_ANTI_CLOCKWISE),
        (ord("q"), Input.QUIT)
    ]
)
def test_run_transforms_input_to_expected_enum(input_ord: int, expected_input: Input) -> None:
    # Arrange.
    stdscr = unittest.mock.create_autospec(curses.window, spec_set=True)
    stdscr.getch.return_value = input_ord

    input_handler = unittest.mock.create_autospec(InputHandler, spec_set=True)
    input_thread = InputThread(stdscr, input_handler)

    # Act.
    input_thread.start()
    input_thread.join(0.005)
    input_thread.stop()

    # Assert.
    input_handler.handle.assert_called_with(expected_input)
