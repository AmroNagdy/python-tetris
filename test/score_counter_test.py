import pytest

from src.score_counter import ScoreCounter


@pytest.mark.parametrize(
    "rows_cleared,expected_score",
    [
        (1, 40),
        (2, 100),
        (3, 300),
        (4, 1200)
    ]
)
def test_update_score_adds_score_given_rows_cleared_is_valid(rows_cleared: int, expected_score: int) -> None:
    # Arrange.
    score_counter = ScoreCounter()

    # Act.
    score_counter.update_score(rows_cleared)

    # Assert.
    assert score_counter.get_total_score() == expected_score


def test_update_score_keeps_running_total_score_given_rows_cleared_in_succession() -> None:
    # Arrange.
    score_counter = ScoreCounter()

    # Act.
    score_counter.update_score(1)
    score_counter.update_score(2)
    score_counter.update_score(3)

    # Assert.
    assert score_counter.get_total_score() == 40 + 100 + 300


@pytest.mark.parametrize(
    "invalid_rows_cleared",
    [0, -1, 5, 100]
)
def test_update_score_raises_value_error_given_invalid_rows_cleared(invalid_rows_cleared: int) -> None:
    # Arrange.
    score_counter = ScoreCounter()

    # Act & Assert.
    with pytest.raises(ValueError):
        score_counter.update_score(invalid_rows_cleared)
