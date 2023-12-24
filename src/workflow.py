from ColumnType import ColumnType
from Cell import Cell
from tabulate import tabulate
from columns import columns

API_RESULT = "https://www.linkedin.com/in/kareemamin/"
rowData = {}

def refreshUI():
    colValues = []
    rowValues = []

    for colId in columns:
        colValues.append(columns[colId])
        if colId in rowData:
            rowValues.append(rowData[colId])
        elif columns[colId].type == ColumnType.BASIC:
            rowValues.append("")
        else:
            rowValues.append("MISSING_INPUT")

    print(tabulate([rowValues], headers=colValues))
    print()

def getOrderedColumnDependencies(updatedCell):
    currColId = updatedCell.colId
    orderedDependencies = []
    found = True
    while found:
        found = False
        for colId in columns:
            if currColId in columns[colId].dependencies:
                orderedDependencies.append(colId)
                currColId = colId
                found = True
                break
    return orderedDependencies

# set to loading any cells that directly depend on current cell
def setLoadingStatus(currColId):
    for colId in columns:
        if currColId in columns[colId].dependencies:
            rowData[colId] = Cell(colId, "LOADING")

def runWorkflowForRow(updatedCell):
    rowData[updatedCell.colId] = updatedCell
    shouldContinue = True
    changesToOtherCells = False
    for colId in getOrderedColumnDependencies(updatedCell):
        if not shouldContinue:
            break
        if columns[colId].type == ColumnType.BASIC:
            continue
        for dep in columns[colId].dependencies:
            if dep not in rowData:
                shouldContinue = False
                break
        if not shouldContinue:
            break
        if columns[colId].type == ColumnType.FORMULA:
            stringsToConcatenate = []
            for dep in columns[colId].dependencies:
                if rowData[dep].apiResult:
                    stringsToConcatenate.append(rowData[dep].apiResult)
                else:
                    stringsToConcatenate.append(rowData[dep].display)
            newCellVaue = " ".join(stringsToConcatenate)
            rowData[colId] = Cell(colId, " ".join(stringsToConcatenate))
        else:
            rowData[colId] = Cell(colId, columns[colId].message, API_RESULT)
        
        setLoadingStatus(colId)
        
        changesToOtherCells = True
        refreshUI()
    
    if not changesToOtherCells:
        refreshUI()

runWorkflowForRow(Cell(1, "Kareem"))
runWorkflowForRow(Cell(2, "Amin"))
runWorkflowForRow(Cell(3, "Clay"))