from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QVBoxLayout, QGroupBox, QPushButton, QLineEdit, QTabWidget, QLabel, QComboBox, QFormLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

from TableGUI import TableData
from PlotGraph import Plot_Graph
from GraphPlot import GraphPlot
from ToolsWidgets import CalculateError, Hamiltonian, ErrorBars, Terminal_for_table

from Calculator import Operations

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

		self.widgetsLyout = QVBoxLayout()

		toolsTab = QTabWidget()
		self.errorBars = ErrorBars(self.dataTable.index)
		self.errorBars.button.clicked.connect(self.plotGraph)
		toolsTab.addTab(self.errorBars, "Error Bars")
		toolsTab.addTab(Hamiltonian(), "Hamiltonian")
		toolsTab.addTab(CalculateError(), "Errors")
		self.widgetsLyout.addWidget(toolsTab)
		self.graphValues()
		self.formulaEntry()
		self.widgetsLyout.addWidget(Terminal_for_table())


		self.Main.addLayout(dataLyout, 25)
		self.Main.addLayout(self.widgetsLyout, 7)

		self.setLayout(self.Main)

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

		self.splitLyout.addWidget(self.Graph)

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

	def graphValues(self):

		graphics = QGroupBox()
		graphics.setTitle("Graphics")

		lbl12 = QLabel("<h1>X</h1>", self)

		lbl13 = QLabel("<h1>Y</h1>", self)

		self.combo = QComboBox(self)
		for name in self.dataTable.index.values():
			self.combo.addItem(name)

		self.combo1 = QComboBox(self)
		for name in self.dataTable.index.values():
			self.combo1.addItem(name)
		#combo1.activated[int].connect(self.onActivatedY)

		fbox = QFormLayout()
		fbox.addRow(lbl12, self.combo)
		fbox.addRow(lbl13, self.combo1)

		graphics.setLayout(fbox)
		self.widgetsLyout.addWidget(graphics)

	def formulaEntry(self):

		Formula = QGroupBox()
		Formula.setTitle("Formula Entry")

		hbox = QHBoxLayout()
		vbox = QVBoxLayout()

		self.lineEdit = QLineEdit(self)
		runButton = QPushButton("Run", self)
		runButton.clicked.connect(self.formula_click)

		vbox.addWidget(self.lineEdit)
		hbox.addWidget(runButton)
		hbox.addStretch(1)
		vbox.addLayout(hbox)
		Formula.setLayout(vbox)

		self.widgetsLyout.addWidget(Formula)

	@pyqtSlot()
	def formula_click(self):
		table, index = Operations( self.lineEdit.text(), self.dataTable.table, self.dataTable.index ).main()

		self.dataTable.table = table
		self.dataTable.index = index
		self.dataTable.reDoTable()