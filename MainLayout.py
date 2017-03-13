from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QVBoxLayout
from PyQt5.QtCore import Qt

from TableGUI import TableData
from PlotGraph import Plot_Graph
from GraphPlot import GraphPlot

class MainLayout(QWidget):

	def __init__(self):

		super(QWidget, self).__init__()

		self.Main = QHBoxLayout()


		dataLyout = QHBoxLayout()

		self.dataTable = TableData()

		self.splitLyout = QSplitter(Qt.Vertical)
		self.splitLyout.setGeometry(0, 0, 1500, 1000)

		self.splitLyout.addWidget(self.dataTable.tableWidget)
		dataLyout.addWidget(self.splitLyout)

		self.Main.addLayout(dataLyout, 25)

		self.setLayout(self.Main)

	def plotGraph(self):

		try:

			graph = GraphPlot(self.dataTable.table, self.dataTable.index, [0,1])
			self.Graph.setGraph(graph)
		
		except AttributeError:

			self.Graph = Plot_Graph()
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, [0,1])

			self.Graph.setGraph(graph)

			self.splitLyout.addWidget(self.Graph)

	def get_DATA(self):

		return self.dataTable.table, self.dataTable.index 

	def set_DATA(self, table, index):

		self.dataTable.table = table
		self.dataTable.index = index