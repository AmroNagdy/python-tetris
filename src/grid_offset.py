import dataclasses


@dataclasses.dataclass(frozen=True)
class GridOffset:
    """
    A pair of pixel offsets from the top left corner of a grid representing a single pixel's relative position.
    """
    x: int
    y: int

    def __iter__(self):
        return iter((self.x, self.y))
