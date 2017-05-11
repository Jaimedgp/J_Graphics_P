#########################################
#              Table Layout             #
#########################################
#
#   This class create the object with the interface required 
#       to generate a Table Widgets in which the data are going
#       to be introduce.
#
#   Attributes: - The Table widget \ QTableWidget(tableWidget)
#               - Columns values \ dict(table)
#               - Columns index \ dict(index)
#
#   reDoTable: this function update the table widget
#               with the new values and names of the 
#               columns (table, index).
#
#####################################################################

from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QSizePolicy
from PyQt5.QtCore import pyqtSlot

class TableData(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        self.table = {}
        self.index = {}

        self.numRows = 20
        self.numColumns = 10

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.numRows)
        self.tableWidget.setColumnCount(self.numColumns)
        self.tableWidget.move(0,0)

        for n in range(0,10):
            for i in range(0,20):
                self.tableWidget.setItem(i,n, QTableWidgetItem())

    def reDoTable(self):

        if self.numRows == max([i for i in [len(i) for i in self.table.values()]]):
            self.tableWidget.insertRow(self.numRows)
            self.numRows = self.numRows + 1

        if self.numColumns == len(self.index): 
            self.tableWidget.insertColumn(self.numColumns)
            self.numColumns = self.numColumns + 1

        self.tableWidget.setHorizontalHeaderLabels(self.index.values())

        length = 0
        # Largest column's length
        for values in self.table.values():
            if length < len(values):
                length = len(values)

        for n in range(len(self.index)):
            for i in range(length):
                try:
                    self.tableWidget.setItem(i,n, QTableWidgetItem(str(self.table[self.index[n]][i])))
                except IndexError:
                    error = 1
