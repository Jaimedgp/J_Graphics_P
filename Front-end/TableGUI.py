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

	def __init__(self, parent):
		super(QWidget, self).__init__(parent)

		self.makingtable()

		self.tableWidget.move(0,0)

		# table selection change
		self.tableWidget.doubleClicked.connect(self.on_click)

	def makingtable(self):
		# Create table
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(10)
		self.tableWidget.setColumnCount(2)
		for n in range(0,2):
			for i in range(0,10):
				self.tableWidget.setItem(i,n, QTableWidgetItem())

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

	def onChanged(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()