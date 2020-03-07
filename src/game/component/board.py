class Board():

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.array = [[0] * width for _ in range(height)]

    def set(self, coords):
        self.update_array(coords, 1)

    def unset(self, coords):
        self.update_array(coords, 0)

    def update_array(self, coords, array_value):
        for y, x in coords:
            self.array[y][x] = array_value

    def should_set_tetromino(self, coords):
        return self.at_bottom(coords) or self.piece_below(coords)

    def at_bottom(self, coords):
        for y, _ in coords:
            if y + 1 > self.height - 1:
                return True

        return False

    def piece_below(self, coords):
        for y, x in coords:
            if self.array[y + 1][x] == 1:
                return True

        return False
