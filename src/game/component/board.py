class Board():

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.height = height - 1
        self.width = width - 1
        self.array = self.build_2d_array(height, width)

    def build_2d_array(self, height, width):
        return [[0] * width for _ in range(height)]

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
            if y + 1 > self.height:
                return True

        return False

    def piece_below(self, coords):
        for y, x in coords:
            if self.array[y + 1][x] == 1:
                return True

        return False

    def collides(self, coords):
        for y, x in coords:
            if self.array[y][x] == 1:
                return True

        return False

    def clear_full_rows(self):
        self.array = [row for row in self.array if not all(e == 1 for e in row)]
        rows_cleared = self.__height - len(self.array)

        if rows_cleared > 0:
            self.array = self.build_2d_array(rows_cleared, self.__width) + self.array

        return rows_cleared
