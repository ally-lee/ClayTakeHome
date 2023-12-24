class Cell:
    def __init__(self, colId, value):
        self.colId = colId
        self.value = value

    def __repr__(self):
        return self.value