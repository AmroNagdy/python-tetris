import pytest

from input import Input


@pytest.mark.parametrize(
    "a,b,other",
    [
        (Input.MOVE_RIGHT, Input.MOVE_RIGHT, Input.MOVE_LEFT),
        (Input.MOVE_LEFT, Input.MOVE_LEFT, Input.MOVE_RIGHT),
        (Input.DROP, Input.DROP, Input.MOVE_RIGHT),
        (Input.ROTATE_CLOCKWISE, Input.ROTATE_CLOCKWISE, Input.ROTATE_ANTI_CLOCKWISE),
        (Input.ROTATE_ANTI_CLOCKWISE, Input.ROTATE_ANTI_CLOCKWISE, Input.ROTATE_CLOCKWISE),
    ]
)
def test_input_implements_equality(a: Input, b: Input, other: Input) -> None:
    # Act & Assert.
    assert a == b
    assert a != other
    assert b != other


@pytest.mark.parametrize(
    "input,expected_output",
    [
        (Input.MOVE_RIGHT, 1),
        (Input.MOVE_LEFT, 2),
        (Input.DROP, 3),
        (Input.ROTATE_CLOCKWISE, 4),
        (Input.ROTATE_ANTI_CLOCKWISE, 5),
    ]
)
def test_input_hashes_as_expected(input: Input, expected_output: int) -> None:
    # Arrange.
    input_to_output = {
        Input.MOVE_RIGHT: 1,
        Input.MOVE_LEFT: 2,
        Input.DROP: 3,
        Input.ROTATE_CLOCKWISE: 4,
        Input.ROTATE_ANTI_CLOCKWISE: 5
    }

    # Act.
    output = input_to_output[input]

    # Assert.
    assert output == expected_output
