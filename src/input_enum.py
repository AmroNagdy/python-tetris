import enum


class InputEnum(enum.Enum):
    MOVE_RIGHT = 0,
    MOVE_LEFT = 1,
    DROP = 2,
    ROTATE_CLOCKWISE = 3,
    ROTATE_ANTI_CLOCKWISE = 4,
    QUIT = 5
