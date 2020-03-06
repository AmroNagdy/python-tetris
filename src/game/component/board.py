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
