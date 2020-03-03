class Board():

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.array = [[0] * width for _ in range(height)]
