from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QVBoxLayout, QGroupBox, QPushButton, QLineEdit, QTabWidget, QLabel, QComboBox, QFormLayout
from PyQt5.QtCore import pyqtSlot, Qt

from TableGUI import TableData
from PlotGraph import Plot_Graph
from GraphPlot import GraphPlot
from ToolsWidgets import *

from Calculator import Operations

class MainLayout(QWidget):

	def __init__(self):

		super(QWidget, self).__init__()

		self.MainLyout = QHBoxLayout()

		dataLyout = QHBoxLayout()
		self.widgetsLyout = QVBoxLayout()
		
		self.dataTable = TableData()
		self.dataTable.tableWidget.itemChanged.connect(self.changeData)

		self.ErrBar = ErrorBars()
		self.Hamiltonian = Hamiltonian()
		self.CalcError = CalculateError()
		self.GrphAxes = GraphAxes()
		self.Formula = FormulaEntry()
		self.Terminal = Terminal_for_table()

		toolsTab = QTabWidget()
		toolsTab.addTab(self.ErrBar, "Error Bars")
		toolsTab.addTab(self.Hamiltonian, "Hamiltonian")
		toolsTab.addTab(self.CalcError, "Errors")

		self.widgetsLyout.addWidget(toolsTab)
		self.widgetsLyout.addWidget(self.GrphAxes)
		self.widgetsLyout.addWidget(self.Formula)
		self.widgetsLyout.addWidget(self.Terminal)
		
		self.splitLyout = QSplitter(Qt.Vertical)
		self.splitLyout.setGeometry(0, 0, 1500, 1000)
		self.splitLyout.addWidget(self.dataTable.tableWidget)
		dataLyout.addWidget(self.splitLyout)

		self.MainLyout.addLayout(dataLyout, 25)
		self.MainLyout.addLayout(self.widgetsLyout, 7)

		self.setLayout(self.MainLyout)

	def plotLinearGraph(self):

		values = [self.combo.currentIndex(), self.combo1.currentIndex()]

		types = self.errorBars.MainCombo.currentText()
		
		if types == "Fixed value":
			error = float(self.errorBars.value.text())
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)
		
		elif types == "Data column":
			error = self.errorBars.combo.currentText()
			error = self.dataTable.table[error]
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)
		
		elif types == "% of value":
			error = float(self.errorBars.percenteg.text())
			error = [ value* (error/100) for value in self.dataTable.table[str(values[1])] ]
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)

		else:
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values)

		try:
			self.Graph.set_linearGraph(graph)
		except AttributeError:
			self.Graph = Plot_Graph()
			self.Graph.set_linearGraph(graph)

		self.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		self.result.setText(graph.text)

		self.splitLyout.addWidget(self.Graph)

	def saveGraph(self):

		self.Graph.saveGraph()

	def plotGraph(self):

		values = [self.combo.currentIndex(), self.combo1.currentIndex()]

		types = self.errorBars.MainCombo.currentText()
		
		if types == "Fixed value":
			error = float(self.errorBars.value.text())
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)
		
		elif types == "Data column":
			error = self.errorBars.combo.currentText()
			error = self.dataTable.table[error]
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)
		
		elif types == "% of value":
			error = float(self.errorBars.percenteg.text())
			error = [ value* (error/100) for value in self.dataTable.table[str(values[1])] ]
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)

		else:
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values)

		try:
			self.Graph.setGraph(graph)
		except AttributeError:
			self.Graph = Plot_Graph()

		self.Graph.setGraph(graph)
		self.splitLyout.addWidget(self.Graph)

	def plotPepeGraph(self):

		values = [self.combo.currentIndex(), self.combo1.currentIndex()]

		types = self.errorBars.MainCombo.currentText()
		
		if types == "Fixed value":
			error = float(self.errorBars.value.text())
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)
		
		elif types == "Data column":
			error = self.errorBars.combo.currentText()
			error = self.dataTable.table[error]
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)
		
		elif types == "% of value":
			error = float(self.errorBars.percenteg.text())
			error = [ value* (error/100) for value in self.dataTable.table[str(values[1])] ]
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values, error)

		else:
			graph = GraphPlot(self.dataTable.table, self.dataTable.index, values)

		try:
			self.Graph.set_PepepeGraph(graph)
		except AttributeError:
			self.Graph = Plot_Graph()
			self.Graph.set_PepepeGraph(graph)

		self.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		self.result.setText(graph.text)

		self.splitLyout.addWidget(self.Graph)

	@pyqtSlot()
	def changeData(self):

		for item in self.dataTable.tableWidget.selectedItems():
			boolean = True
			while boolean:
				try:
					if item.text() == '':
						if item.row() >= len(self.dataTable.table[self.dataTable.index[item.column()]]):
							self.dataTable.table[self.dataTable.index[item.column()]]							
						else:
							del self.dataTable.table[self.dataTable.index[item.column()]][item.row()]
						boolean = False
					else:
						self.dataTable.table[self.dataTable.index[item.column()]][item.row()] = float(item.text())
						boolean = False
				except IndexError:
					self.dataTable.table[self.dataTable.index[item.column()]].append(float(item.text()))
					boolean = False
				except KeyError:
					self.dataTable.table[str(item.column())] = []
					self.dataTable.index[item.column()] = str(item.column())
					self.ErrBar.set_new_Columns_names(self.dataTable.index)
					self.GrphAxes.setNames(self.dataTable.index)









	@pyqtSlot()
	def formula_click(self):
		table, index = Operations( self.lineEdit.text(), self.dataTable.table, self.dataTable.index ).main()

		self.dataTable.table = table
		self.dataTable.index = index
		self.dataTable.reDoTable()
		self.redoNmaes()