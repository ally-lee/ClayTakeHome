from BasicColumn import BasicColumn
from FormulaColumn import FormulaColumn
from APIColumn import APIColumn
from Cell import Cell
from workflow import runWorkflowForRow

if __name__ == "__main__":
    columns = {
        1: BasicColumn(1, "First Name"),
        2: BasicColumn(2, "Last Name"),
        3: BasicColumn(3, "Company Name"),
        4: FormulaColumn(4, "Google Search Input", ["linkedin.com", 1, 2, 3]),
        5: APIColumn(5, "Google Search", [4], "Search complete", "https://www.linkedin.com/in/kareemamin/"),
        6: FormulaColumn(6, "LinkedIn URL", [5]),
        7: APIColumn(7, "LinkedIn Data", [6], "Profile found", "")
    }
    rowData = {}

    runWorkflowForRow(Cell(1, "Kareem"), rowData, columns)
    runWorkflowForRow(Cell(2, "Amin"), rowData, columns)
    runWorkflowForRow(Cell(3, "Clay"), rowData, columns)