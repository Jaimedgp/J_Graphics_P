#########################################
#		       Table Layout	            #
#########################################
#
#	FALTA EL COMANDO SELF.SHOW()
#
#	This class allows to make all the mathematical operations
#
#	Required: 
#
#	Return: 
#
##############################################################################

from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QSizePolicy
from PyQt5.QtCore import pyqtSlot

class TableData(QWidget):
	""" GUI Table to manage data in the interface """

	def __init__(self):
		
		super(QWidget, self).__init__()

		self.table = {}
		self.index = {}
		
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(20)
		self.tableWidget.setColumnCount(11)
		self.tableWidget.move(0,0)

		for n in range(0,10):
			for i in range(0,20):
				self.tableWidget.setItem(i,n, QTableWidgetItem())
		
		# table selection change
		
	def reDoTable(self):

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