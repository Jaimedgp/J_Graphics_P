#########################################
#		       Main Window	            #
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

from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtGui import QIcon

class Main_Window_GUI(QMainWindow):

	def __init__(self):

		super(QMainWindow, self).__init__()

		self.setGeometry(0, 0, 2000, 1100)
		self.setWindowTitle("Just a Graphics Printer")
		self.setWindowIcon( QIcon("./Photos/JGP(icon).png") )

		self.fileMenuBar()
		self.graphMenuBar()
		self.toolsMenuBar()

	def fileMenuBar(self):

		openAction = QAction('Open file', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open a table from a file')

		saveAction = QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save table')

		saveAs = QAction('Save as', self)
		saveAs.setStatusTip('Save table')

		savepng = QAction('Save Figure', self)
		saveAs.setStatusTip('Save Figure')

		saveTex = QAction('Export to LaTeX', self)
		saveTex.setStatusTip('Export table to LaTex code')

		exitAction = QAction('Quit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAs)
		fileMenu.addAction(savepng)
		fileMenu.addAction(saveTex)
		fileMenu.addAction(exitAction)

	def graphMenuBar(self):

		Graph = QAction('Graphic', self)
		Graph.setShortcut('Ctrl+G')

		linearGraph = QAction('Linear', self)
		linearGraph.setStatusTip('y = a*x + b')

		logGraph = QAction('Logarithmic', self)
		logGraph.setStatusTip('a*log(x) + b')

		expGraph = QAction('Exponential', self)
		expGraph.setStatusTip('b * e^(a*x)')

		polyGraph = QAction('Polynomial', self)

		pepepeGraph = QAction('Pepe', self)
		pepepeGraph.setStatusTip('a*x^m')

		self.statusBar()

		menubar = self.menuBar()
		graphMenu = menubar.addMenu('&Curve Fit')
		graphMenu.addAction(Graph)
		graphMenu.addAction(linearGraph)
		graphMenu.addAction(logGraph)
		graphMenu.addAction(expGraph)
		graphMenu.addAction(polyGraph)
		graphMenu.addAction(pepepeGraph)

	def toolsMenuBar(self):

		diffCalculator = QAction('Derivative', self)
		diffCalculator.setStatusTip('Calculate the derivative between two columns')

		refreshed = QAction('Refresh Window', self)
		refreshed.setShortcut('Ctrl+R')

		self.statusBar()

		menubar = self.menuBar()
		toolsMenu = menubar.addMenu('&Tools')
		toolsMenu.addAction(diffCalculator)
		toolsMenu.addAction(refreshed)

	def addLayout(self, layout):

		self.setCentralWidget(layout)