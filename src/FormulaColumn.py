from Column import Column
from ColumnType import ColumnType

class FormulaColumn(Column):
    def __init__(self, id, name, dependencies):
        super().__init__(id, name, ColumnType.FORMULA, dependencies)