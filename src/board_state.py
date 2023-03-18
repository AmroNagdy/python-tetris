import enum

from src.tetromino import Tetromino, ITetromino, ZTetromino, TTetromino, STetromino, OTetromino, LTetromino, JTetromino


class BoardState(int, enum.Enum):
    EMPTY = 0,
    I = 1,
    J = 2,
    L = 3,
    O = 4,
    S = 5,
    T = 6,
    Z = 7

    @staticmethod
    def get_state(tetromino: Tetromino) -> "BoardState":
        tetromino_type = type(tetromino)

        if tetromino_type is ITetromino:
            return BoardState.I
        elif tetromino_type is JTetromino:
            return BoardState.J
        elif tetromino_type is LTetromino:
            return BoardState.L
        elif tetromino_type is OTetromino:
            return BoardState.O
        elif tetromino_type is STetromino:
            return BoardState.S
        elif tetromino_type is TTetromino:
            return BoardState.T
        elif tetromino_type is ZTetromino:
            return BoardState.Z
        else:
            raise ValueError(f"Unrecognised tetromino type: {tetromino_type}.")
