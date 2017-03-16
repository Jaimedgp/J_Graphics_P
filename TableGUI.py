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

		self.table = {} #{'10': [], '1': [], '0': [], '3': [], '2': [], '5': [], '4': [], '7': [], '6': [], '9': [], '8': []}
		self.index = {} #{0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}
		self.makingtable()

		self.tableWidget.move(0,0)

		# table selection change
		self.tableWidget.itemChanged.connect(self.on_click)

	def makingtable(self):

		# Create table
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(20)
		self.tableWidget.setColumnCount(11)
		self.tableWidget.setHorizontalHeaderLabels(self.index.values())
		for n in range(0,10):
			for i in range(0,20):
				self.tableWidget.setItem(i,n, QTableWidgetItem())

	@pyqtSlot()
	def on_click(self):
		for item in self.tableWidget.selectedItems():
			boolean = True
			while boolean:
				try:
					if item.text() == '':
						if item.row() >= len(self.table[self.index[item.column()]]):
							self.table[self.index[item.column()]]							
						else:
							del self.table[self.index[item.column()]][item.row()]
						boolean = False
					else:
						self.table[self.index[item.column()]][item.row()] = float(item.text())
						boolean = False
				except IndexError:
					self.table[self.index[item.column()]].append(float(item.text()))
					boolean = False
				except KeyError:
					self.table[str(item.column())] = []
					self.index[item.column()] = str(item.column())


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