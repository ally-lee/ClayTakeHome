from Column import Column
from ColumnType import ColumnType

class BasicColumn(Column):
    def __init__(self, id, name):
        super().__init__(id, name, ColumnType.BASIC, [])