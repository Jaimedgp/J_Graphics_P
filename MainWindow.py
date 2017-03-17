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

from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QFileDialog, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon
import sys

from MainLayout import MainLayout
from MainTabses import TabMain

from OpenScript import Open_file_CSV
from SaveScript import saveCSV, saveLaTex

class Main_Window_GUI(QMainWindow):

	def __init__(self):

		super(QMainWindow, self).__init__()

		self.setGeometry(0, 0, 2000, 1100)
		self.setWindowTitle("Just a Graphics Printer")
		self.setWindowIcon( QIcon("/home/jaime/J_Graphics_P/Photos/JGP(icon).png") )

		self.fileMenuBar()
		self.graphMenuBar()
		self.toolsMenuBar()

	def fileMenuBar(self):

		openProject = QAction('Open Project', self)
		openProject.setShortcut('Ctrl+T')
		openProject.triggered.connect(self.openAProject)

		deleteProject = QAction('Delete Project', self)
		deleteProject.setShortcut('Ctrl+W')
		deleteProject.triggered.connect(self.closeEvent)

		openAction = QAction('Open file', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open a table from a file')
		openAction.triggered.connect(self.openFile)

		saveAction = QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save table')
		saveAction.triggered.connect(self.save)

		saveAs = QAction('Save as', self)
		saveAs.setStatusTip('Save table')

		savepng = QAction('Save Figure', self)
		savepng.setStatusTip('Save Figure')
		savepng.triggered.connect(self.saveFigure)

		saveTex = QAction('Export to LaTeX', self)
		saveTex.setStatusTip('Export table to LaTex code')
		saveTex.triggered.connect(self.saveIntoTex)

		exitAction = QAction('Quit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openProject)
		fileMenu.addAction(deleteProject)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAs)
		fileMenu.addAction(savepng)
		fileMenu.addAction(saveTex)
		fileMenu.addAction(exitAction)

	def graphMenuBar(self):

		Graph = QAction('Graphic', self)
		Graph.setShortcut('Ctrl+G')
		Graph.triggered.connect(self.graph)

		linearGraph = QAction('Linear', self)
		linearGraph.setStatusTip('y = a*x + b')
		linearGraph.triggered.connect(self.linearGraph)

		logGraph = QAction('Logarithmic', self)
		logGraph.setStatusTip('a*log(x) + b')

		expGraph = QAction('Exponential', self)
		expGraph.setStatusTip('b * e^(a*x)')

		polyGraph = QAction('Polynomial', self)

		pepepeGraph = QAction('Pepe', self)
		pepepeGraph.setStatusTip('a*x^m')
		pepepeGraph.triggered.connect(self.pepepeGraph)

		details = QAction('Show Details', self)

		self.statusBar()

		menubar = self.menuBar()
		graphMenu = menubar.addMenu('&Curve Fit')
		graphMenu.addAction(Graph)
		graphMenu.addAction(linearGraph)
		graphMenu.addAction(logGraph)
		graphMenu.addAction(expGraph)
		graphMenu.addAction(polyGraph)
		graphMenu.addAction(pepepeGraph)
		graphMenu.addAction(details)

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

	def openAProject(self):
		mainLayout2 = MainLayout()

		TAB.append(mainLayout2)

		tabLayout.addTabs(mainLayout2)
	
	def closeProject(self):

		if not TAB[tabLayout.currentIndex()].dataSaved:

			reply = QMessageBox.information(self, ' ', "Save changes before closing?", QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard, QMessageBox.Save)

			if reply == QMessageBox.Save:

				self.save()

			
			elif reply == QMessageBox.Discard:
				
				del TAB[tabLayout.currentIndex()]
				
				tabLayout.deleteTabs(tabLayout.currentIndex())

		else:

			del TAB[tabLayout.currentIndex()]
				
			tabLayout.deleteTabs(tabLayout.currentIndex())

	def openFile(self):
		fileName = QFileDialog.getOpenFileName(self, 'Open file', '/home/jaime', 'Text File (*.csv *.txt)')

		if '/home/jaime' in fileName[0]:

			table, index = Open_file_CSV(fileName[0])

			TAB[tabLayout.currentIndex()].dataTable.table = table
			TAB[tabLayout.currentIndex()].dataTable.index = index

			TAB[tabLayout.currentIndex()].dataTable.reDoTable()

	def save(self):

		fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Calc files (*.csv *.txt)"))
		fname = fname.split(',')[0]
		fname = fname.split('(u')
		fname = fname[1].split("'")

		saveCSV(TAB[tabLayout.currentIndex()].dataTable.table, TAB[tabLayout.currentIndex()].dataTable.index, fname[1])

		TAB[tabLayout.currentIndex()].dataSaved = True

	def saveIntoTex(self):

		text, ok = QInputDialog.getText(self, 'Export LaTex', '    Columns <h6>e.j."1,2" for columns C1 and C2<\h6> or "all" for all table:')
		if ok:
			fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "LaTex files (*.tex)"))
			fname = fname.split(',')[0]
			fname = fname.split('(u')
			fname = fname[1].split("'")

		if text == 'all':
			saveLaTex(TAB[tabLayout.currentIndex()].dataTable.table, TAB[tabLayout.currentIndex()].dataTable.index, TAB[tabLayout.currentIndex()].dataTable.index.keys(), fname[1])
		else:
			 
			saveLaTex(TAB[tabLayout.currentIndex()].dataTable.table, TAB[tabLayout.currentIndex()].dataTable.index, eval(text), fname[1])

	def saveFigure(self):

		TAB[tabLayout.currentIndex()].saveGraph()		

	def graph(self):

		TAB[tabLayout.currentIndex()].plotGraph()

	def linearGraph(self):

		TAB[tabLayout.currentIndex()].plotLinearGraph()	

	def pepepeGraph(self):

		TAB[tabLayout.currentIndex()].plotPepeGraph()

	def closeEvent(self, event):

		boolean = True

		for tab in TAB:
			if not tab.dataSaved:
				boolean = False

		if boolean:
		
			event.accept()

		else:

			reply = QMessageBox.information(self, ' ', "Save changes before closing?", QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard, QMessageBox.Save)

			if reply == QMessageBox.Save:

				for tab in TAB:
					if not tab.dataSaved:

						fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Calc files (*.csv *.txt)"))
						fname = fname.split(',')[0]
						fname = fname.split('(u')
						fname = fname[1].split("'")

						saveCSV(tab.dataTable.table, tab.dataTable.index, fname[1])

				event.accept()

			elif reply == QMessageBox.Discard:
				event.accept()
			else:
				event.ignore()



	def addLayout(self, layout):

		self.setCentralWidget(layout)


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

if __name__ == '__main__':

	app = QApplication(sys.argv)

	tabLayout = TabMain()

	mainLayout = MainLayout()

	TAB = [mainLayout]

	tabLayout.addTabs(mainLayout)

	ex = Main_Window_GUI()
	ex.addLayout(tabLayout)
	ex.show()
	sys.exit(app.exec_())