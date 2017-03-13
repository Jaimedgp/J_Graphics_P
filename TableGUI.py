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

		self.makingtable()

		self.tableWidget.move(0,0)
		self.table = {'0':[], '1':[]}
		self.index = {0:'0', 1:'1'} 

		# table selection change
		self.tableWidget.itemChanged.connect(self.on_click)

	def makingtable(self):

		# Create table
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(20)
		self.tableWidget.setColumnCount(10)
		for n in range(0,10):
			for i in range(0,20):
				self.tableWidget.setItem(i,n, QTableWidgetItem())

	@pyqtSlot()
	def on_click(self):
		for item in self.tableWidget.selectedItems():
			boolean = True
			while boolean:
				try:
					self.table[self.index[item.column()]][item.row()] = float(item.text())
					boolean = False
				except IndexError:
					self.table[self.index[item.column()]].append(float(item.text()))
					boolean = False
				except KeyError:
					self.index[2] = '2'
					self.table['2'] = []
				except ValueError:
					error = 1

	def reDoTable(self):
		for n in range(len(self.index)):
			for i in range(len(self.table[self.index[0]])):
				self.tableWidget.setItem(i,n, QTableWidgetItem(str(self.table[self.index[n]][i])))

	def get_DATA(self):
		return self.table, self.index