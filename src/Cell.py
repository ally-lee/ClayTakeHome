class Cell:
    def __init__(self, colId, display, apiResult=None):
        self.colId = colId
        self.display = display
        self.apiResult = apiResult

    def __repr__(self):
        return self.display