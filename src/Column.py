from ColumnType import ColumnType

class Column:
    def __init__(self, id, name, type, dependencies):
        assert isinstance(type, ColumnType)
        self.id = id
        self.name = name
        self.type = type
        self.dependencies = dependencies
    
    def __repr__(self):
        return "{} ({})".format(self.name, self.type.name)