from Column import Column
from ColumnType import ColumnType

class APIColumn(Column):
    def __init__(self, id, name, dependencies, message, result):
        super().__init__(id, name, ColumnType.API, dependencies)
        self.message = message
        self.result = result