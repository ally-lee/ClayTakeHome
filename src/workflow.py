from BasicColumn import BasicColumn
from FormulaColumn import FormulaColumn
from APIColumn import APIColumn
from ColumnType import ColumnType
from Cell import Cell
from tabulate import tabulate

API_RESULT = "https://www.linkedin.com/in/kareemamin/"

def refreshUI(rowData, columns):
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

def getOrderedColumnDependencies(updatedCell, columns):
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

# set to loading any API cells that directly depend on current cell
def setLoadingStatus(currColId, rowData, columns):
    loadingStatusSet = False
    for colId in columns:
        if columns[colId].type == ColumnType.API and currColId in columns[colId].dependencies:
            rowData[colId] = Cell(colId, "LOADING")
            loadingStatusSet = True
    return loadingStatusSet

def runWorkflowForRow(updatedCell, rowData, columns):
    rowData[updatedCell.colId] = updatedCell
    shouldContinue = True
    for colId in getOrderedColumnDependencies(updatedCell, columns):
        if not shouldContinue:
            break
        for dep in columns[colId].dependencies:
            if not isinstance(dep, str) and dep not in rowData:
                shouldContinue = False
                break
        if not shouldContinue:
            break

        if columns[colId].type == ColumnType.FORMULA:
            stringsToConcatenate = []
            for dep in columns[colId].dependencies:
                if isinstance(dep, str):
                    stringsToConcatenate.append(dep)
                elif rowData[dep].apiResult:
                    stringsToConcatenate.append(rowData[dep].apiResult)
                else:
                    stringsToConcatenate.append(rowData[dep].display)
            newCellVaue = " ".join(stringsToConcatenate)
            rowData[colId] = Cell(colId, " ".join(stringsToConcatenate))
        else:
            rowData[colId] = Cell(colId, columns[colId].message, API_RESULT)
        
        loadingStatusSet = setLoadingStatus(colId, rowData, columns)
        
        if loadingStatusSet:
            refreshUI(rowData, columns)

    refreshUI(rowData, columns)