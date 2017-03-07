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

from TableGUI import TableData
from PlotGraph import Plot_Graph
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QVBoxLayout
from PyQt5.QtCore import Qt

class MainLayout(QWidget):
	""" Main Layout of the interface """

	def __init__(self):

		super(QWidget, self).__init__()

		self.MainLayout = QHBoxLayout()

		self.setLayout(self.MainLayout)

	def widgetToolLyout(self):

		widgetLyout = QVBoxLayout()

		#Graphics = GraphElements()
		#Formula = FormulaEntry()
		#Terminal = Terminal()

		#widgetLyout.addWidget(Graphics)
		#widgetLyout.addWidget(Formula)
		#widgetLyout.addWidget(Terminal)

		self.MainLayout.addLayout(widgetLyout, 7)

	def showDataLyout(self):

		showLyout = QHBoxLayout()

		splitLyout = QSplitter(Qt.Vertical)
		splitLyout.setGeometry(0, 0, 1500, 1000)
		splitLyout.addWidget(TableData(self).tableWidget)

		graph = Plot_Graph()
		splitLyout.addWidget(graph)

		showLyout.addWidget(splitLyout)

		self.MainLayout.addLayout(showLyout, 25)
