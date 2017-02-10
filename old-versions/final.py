"""
	JDG (Just a Graphics' Printer) 

	This program has been develop by Jaime Diez Gonzalez-Pardo in Python in 
	order to facilitate operations in performing laboratory practice

													Version: Enero 2017
"""

from PyQt5.QtWidgets import (QToolTip, QMessageBox, QDesktopWidget, QInputDialog, QHBoxLayout, QFrame, QSplitter, QStyleFactory, 
	QMainWindow, QTabWidget, QTextEdit, QAction, QApplication, QWidget, QFormLayout, QPushButton, QLineEdit, QTableWidget,
	QTableWidgetItem, QVBoxLayout, QFileDialog, QSizePolicy, QCalendarWidget, QLabel, QProgressBar, QCheckBox, QComboBox)
from PyQt5.QtGui import QFont, QIcon 
from PyQt5.QtCore import QCoreApplication, pyqtSlot, Qt, QDate, QBasicTimer
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from JGP1 import *
import sys
import numpy as np
import matplotlib.pyplot as plt
import os # import os Miscellaneous operating system interfaces

class GUI(QMainWindow):

	def __init__(self):
		super(GUI,self).__init__()

		self.menuBarsus()

		self.setGeometry(0, 0, 1950, 1056)
		self.setWindowTitle('Just a Graphics Printer')
		self.setWindowIcon(QIcon('./Desktop/JGP(GUI)/JGP(icon).png'))

		self.splitters1_widget = MySplitterWidget1(self)
		self.setCentralWidget(self.splitters1_widget)

		#self.table_widget = MyTableWidget(self)
		#self.setCentralWidget(self.table_widget)
		
		self.show()

	def menuBarsus(self):
		
		newproject = QAction('New Project', self)
		newproject.setShortcut('Ctrl+P')
		newproject.setStatusTip('Create a new project')
		newproject.triggered.connect(self.newproject)

		newAction = QAction('New file', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('Create a new table')
		newAction.triggered.connect(self.newfile)

		openAction = QAction('Open file', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open a table from a file')
		openAction.triggered.connect(self.openfile)

		eraseProject = QAction('Erase Project', self)
		eraseProject.setShortcut('Ctrl+W')
		eraseProject.setStatusTip('Erase this project')
		eraseProject.triggered.connect(self.eraseProj)

		saveAction = QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save table')
		saveAction.triggered.connect(self.saveCSV)

		saveAs = QAction('Save as', self)
		#saveAs.setShortcut('Ctrl+S')
		saveAs.setStatusTip('Save table')
		saveAs.triggered.connect(self.saveAs)

		saveTex = QAction('Export to LaTex', self)
		#newproject.setShortcut('Ctrl+P')
		saveTex.setStatusTip('Export table to LaTex code')
		saveTex.triggered.connect(self.saveTex)

		exitAction = QAction('Quit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newproject)
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(eraseProject)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAs)
		fileMenu.addAction(saveTex)
		fileMenu.addAction(exitAction)

		addValue = QAction('Add Value', self)
		#addValue.setShortcut('Ctrl+N')
		addValue.setStatusTip('Add a new value on the table')
		"""addValue.triggered.connect(save(Path, Title))"""

		delValue = QAction('Delete Value', self)
		#openAction.setShortcut('Ctrl+O')
		delValue.setStatusTip('delete a value from a column')
		"""saveAction.triggered.connect(save(Path, Title))"""

		chngValue = QAction('Change Value', self)
		#saveAction.setShortcut('Ctrl+S')
		chngValue.setStatusTip('Change the value of a column element')
		"""saveAction.triggered.connect(save(Path, Title))"""

		addColmn = QAction('Add Column', self)
		#saveAction.setShortcut('Ctrl+S')
		addColmn.setStatusTip('Add a new column')
		"""saveAction.triggered.connect(save(Path, Title))"""

		delColm = QAction('Delete column', self)
		#saveAction.setShortcut('Ctrl+S')
		delColm.setStatusTip('Delete a column')
		"""saveAction.triggered.connect(save(Path, Title))"""

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Edit')
		fileMenu.addAction(addValue)
		fileMenu.addAction(delValue)
		fileMenu.addAction(chngValue)
		fileMenu.addAction(addColmn)
		fileMenu.addAction(delColm)

		Graph = QAction('Graphic', self)
		Graph.setShortcut('Ctrl+G')
		#Graph.setStatusTip('y = a*x + b')
		Graph.triggered.connect(self.graph)

		details = QAction('Show Details', self)
		#Graph.setShortcut('Ctrl+G')
		#Graph.setStatusTip('y = a*x + b')
		details.triggered.connect(self.detail)

		Scrat = QAction('Scratter', self)
		#Scrat.setShortcut('Ctrl+G')
		#Graph.setStatusTip('y = a*x + b')
		Scrat.triggered.connect(self.graph)

		linearGraph = QAction('Linear', self)
		#newAction.setShortcut('Ctrl+N')
		linearGraph.setStatusTip('y = a*x + b')
		linearGraph.triggered.connect(self.linearing)

		logGraph = QAction('Logarithmic', self)
		#openAction.setShortcut('Ctrl+O')
		logGraph.setStatusTip('a*log(x) + b')
		logGraph.triggered.connect(self.logarithmic)

		expGraph = QAction('Exponential', self)
		#saveAction.setShortcut('Ctrl+S')
		expGraph.setStatusTip('b * e^(a*x)')
		expGraph.triggered.connect(self.exponential)

		polyGraph = QAction('Polynomial', self)
		#polyGraph.setShortcut('Ctrl+S')
		#polyGraph.setStatusTip('b * e^(a*x)')
		polyGraph.triggered.connect(self.polynomial)

		sinusoidalGraph = QAction('Sinusoidal', self)
		#sinusoidalGraph.setShortcut('Ctrl+S')
		#sinusoidalGraph.setStatusTip('b * e^(a*x)')
		sinusoidalGraph.triggered.connect(self.sinusoidal)

		generalGraph = QAction('fit 1', self)
		#generalGraph.setShortcut('Ctrl+S')
		#generalGraph.setStatusTip('b * e^(a*x)')
		#generalGraph.triggered.connect(self.general)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Curve Fit')
		fileMenu.addAction(Graph)
		fileMenu.addAction(Scrat)
		fileMenu.addAction(linearGraph)
		fileMenu.addAction(logGraph)
		fileMenu.addAction(expGraph)
		fileMenu.addAction(polyGraph)
		fileMenu.addAction(sinusoidalGraph)
		fileMenu.addAction(generalGraph)
		fileMenu.addAction(details)

		formulaEntry = QAction('Formula Entry', self)
		formulaEntry.setShortcut('Ctrl+F')
		formulaEntry.setStatusTip('Operate between columns')
		formulaEntry.triggered.connect(self.formulaOperator)

		errorsCalculator = QAction('Error Calculator', self)
		errorsCalculator.setShortcut('Ctrl+E')
		errorsCalculator.setStatusTip('Calculate the error from an equation')
		errorsCalculator.triggered.connect(self.calculate)

		diffCalculator = QAction('Derivative', self)
		#diffCalculator.setShortcut('Ctrl+E')
		diffCalculator.setStatusTip('Calculate the derivative between two columns')
		diffCalculator.triggered.connect(self.differential)

		refreshed = QAction('Refresh Window', self)
		refreshed.setShortcut('Ctrl+R')
		refreshed.triggered.connect(self.refresh)

		hamiltonial = QAction('Hamiltonial', self)
		#hamiltonial.setShortcut('Ctrl+R')
		hamiltonial.triggered.connect(self.hamil)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Tools')
		fileMenu.addAction(formulaEntry)
		fileMenu.addAction(errorsCalculator)
		fileMenu.addAction(hamiltonial)
		fileMenu.addAction(diffCalculator)
		fileMenu.addAction(refreshed)

	def sinusoidal(self):
		projectes.add_Function("graph")
		projectes.add_Function("Sinusoidal")
		if "Linear" in projectes.get_Function():
			projectes.del_Function("Linear")
		if "Exponential" in projectes.get_Function():
			projectes.del_Function("Exponential")
		if "Logarithmic" in projectes.get_Function():
			projectes.del_Function("Logarithmic")
		self.refresh()

	def differential(self):
		text, ok = QInputDialog.getText(self, 'Derivadas', '    Columns <h6>e.j."1,2" for columns C1 and C2<\h6>:')
		if ok:
			text = eval(text)
			Inteface().differential(text)
			
	def polynomial(self):
		projectes.add_Function("Polynomial")
		if "Linear" in projectes.get_Function():
			projectes.del_Function("Linear")
		if "Exponential" in projectes.get_Function():
			projectes.del_Function("Exponential")
		if "Logarithmic" in projectes.get_Function():
			projectes.del_Function("Logarithmic")

		text, ok = QInputDialog.getText(self, 'Polynomial', 'Grade:')
		if ok:
			projectes.set_index(text)

		self.refresh()

	def detail(self):
		Inteface().details()

	def hamil(self):
		projectes.add_Function("Hamilton")
		self.refresh()

	def calculate(self):
		projectes.add_Function("Calculator")
		self.refresh()

	def graph(self):
		projectes.add_Function("graph")
		projectes.add_Function("Scratter")
		if "Linear" in projectes.get_Function():
			projectes.del_Function("Linear")
		if "Exponential" in projectes.get_Function():
			projectes.del_Function("Exponential")
		if "Logarithmic" in projectes.get_Function():
			projectes.del_Function("Logarithmic")
		self.refresh()

	def logarithmic(self):
		projectes.add_Function("graph")
		projectes.add_Function("Logarithmic")
		if "Linear" in projectes.get_Function():
			projectes.del_Function("Linear")
		if "Exponential" in projectes.get_Function():
			projectes.del_Function("Exponential")
		self.refresh()

	def exponential(self):
		projectes.add_Function("graph")		
		projectes.add_Function("Exponential")
		if "Linear" in projectes.get_Function():
			projectes.del_Function("Linear")
		if "Logarithmic" in projectes.get_Function():
			projectes.del_Function("Logarithmic")
		self.refresh()

	def linearing(self):
		projectes.add_Function("graph")
		projectes.add_Function("Linear")
		if "Exponential" in projectes.get_Function():
			projectes.del_Function("Exponential")
		if "Logarithmic" in projectes.get_Function():
			projectes.del_Function("Logarithmic")
		self.refresh()

	def saveAs(self):
		fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Calc files (*.csv *.txt)"))
		fname = fname.split(',')[0]
		fname = fname.split('(u')
		fname = fname[1].split("'")
		projectes.set_Path(fname[1])
		Inteface().savingCSV()

	def saveCSV(self):
		try:
			Inteface().savingCSV()
		except IndexError:
			fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Calc files (*.csv *.txt)"))
			fname = fname.split(',')[0]
			fname = fname.split('(u')
			fname = fname[1].split("'")
			projectes.set_Path(fname[1])
			Inteface().savingCSV()

	def saveTex(self):
		text, ok = QInputDialog.getText(self, 'Export LaTex', '    Columns <h6>e.j."1,2" for columns C1 and C2<\h6> or "all" for all table:')
		if ok:
			fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "LaTex files (*.tex)"))
			fname = fname.split(',')[0]
			fname = fname.split('(u')
			fname = fname[1].split("'")
		Inteface().savingTex(fname[1], text)

	def formulaOperator(self):

		projectes.add_Function("Formulation")
		self.refresh()

	def newproject(self):
		global numtabses
		numtabses +=1
		self.refresh()

	def eraseProj(self):
		global numtabses
		numtabses -=1
		self.refresh()

	def newfile(self):
		self.refresh()

		self.show()

	def openfile(self):
		global numtabses
		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/jaime', 'Text File (*.csv *.txt)')


		Inteface().openingFile(fname[0])

		numtabses +=1
		self.refresh()

		self.show()

	def closeEvent(self, event):

		reply = QMessageBox.information(self, ' ', "Save changes before closing?", QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard, QMessageBox.Save)

		if reply == QMessageBox.Save:
			saving = True
			while saving:
				try:
					Inteface().savingCSV()
					saving = False
				except IndexError:
					fname = str(QFileDialog.getExistingDirectory(self, 'Open file'))
					projectes.set_Title('Sin titulo')
					projectes.set_Path(fname+'/')
			event.accept()
		elif reply == QMessageBox.Discard:
			event.accept()
		else:
			event.ignore()

	def refresh(self):
		self.splitters1_widget = MySplitterWidget1(self)
		self.setCentralWidget(self.splitters1_widget)

class MySplitterWidget1(QWidget):

	def __init__(self, parent):
		global numtabses
		super(QWidget, self).__init__()

		self.table_widget = MyTableWidget(self, numtabses)
		self.widgets = OtherSplitterWidget()
		self.table_widget.setGeometry(0,0,1300, 1000)

		hbox = QHBoxLayout(self)

		splitter1 = QSplitter(Qt.Horizontal)
		splitter1.addWidget(self.table_widget)
		splitter1.addWidget(self.widgets)
		#splitter1.setGeometry(0, 0, 1500, 1500)

		hbox.addWidget(splitter1)
		self.setLayout(hbox)

	#def onChanged(self, text):
	#	self.lbl.setText(text)
	#	self.lbl.adjustSize() 

class MySplitterWidget(QWidget):

	def __init__(self, parent):
		super(QWidget, self).__init__(parent)

		self.createTable()

		if "graph" in projectes.get_Function() and not None in projectes.get_Represent():
			self.plot = PlotCanvas(self, width=5, height=4)
		else:
			self.plot = QFrame(self)
			self.plot.setFrameShape(QFrame.StyledPanel)


		hbox = QHBoxLayout(self)

		splitter1 = QSplitter(Qt.Vertical)
		splitter1.setGeometry(0, 0, 1500, 900)
		splitter1.addWidget(self.tableWidget)
		splitter1.addWidget(self.plot)
		#splitter1.setGeometry(0, 0, 1500, 1500)

		hbox.addWidget(splitter1)
		self.setLayout(hbox)

	def createTable(self):
			
		self.makingtable()

		self.tableWidget.move(0,0)

		# table selection change
		self.tableWidget.doubleClicked.connect(self.on_click)

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

	def onChanged(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize() 

	def makingtable(self):
		length = 0
		try: # handling exception
			length = len(projectes.get_Table()[0].get_list_values())

			for i in range(projectes.get_Len_Table()-1):
				if len(projectes.get_Table()[i].get_list_values()) < len(projectes.get_Table()[i+1].get_list_values()):
					length = len(projectes.get_Table()[i+1].get_list_values())

			# Create table
			self.tableWidget = QTableWidget()
			self.tableWidget.setRowCount(length)
			self.tableWidget.setColumnCount(projectes.get_Len_Table())
			titles = "self.tableWidget.setHorizontalHeaderLabels((projectes.get_Table()[0].get_name()"
			for i in range(1,projectes.get_Len_Table()):
				titles += ", projectes.get_Table()["+str(i)+"].get_name()"
			titles += "))"
			eval(titles)

			for n in range(projectes.get_Len_Table()-1):
				for i in range(length):
					try:
						self.tableWidget.setItem(i,n, QTableWidgetItem(str(projectes.get_Table()[n].get_values(i))))
					except IndexError:
						self.tableWidget.setItem(i,n, QTableWidgetItem(' '))
					try:
						self.tableWidget.setItem(i,n+1, QTableWidgetItem(str(projectes.get_Table()[n+1].get_values(i))))
					except IndexError:
						self.tableWidget.setItem(i,n+1, QTableWidgetItem(' '))

		except (NameError, IndexError):
			self.tableWidget = QTableWidget()
			self.tableWidget.setRowCount(10)
			self.tableWidget.setColumnCount(2)
			for n in range(0,2):
				for i in range(0,10):
					self.tableWidget.setItem(i,n, QTableWidgetItem())

class OtherSplitterWidget(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()

		hbox = QHBoxLayout(self)

		self.widgets = MyWidgets()


		self.edit = QTextEdit()
		self.edit.setGeometry(0,0,200,500)
		self.button1 = QPushButton('Add Columns', self)
		self.button1.move(110, 300)
		self.button1.clicked.connect(self.doAddColumns)
		self.button2 = QPushButton('New Table', self)
		self.button2.move(220, 300)
		self.button2.clicked.connect(self.doChangeColumns)

		self.splitter1 = QSplitter(Qt.Horizontal)
		self.splitter1.addWidget(self.button2)
		self.splitter1.addWidget(self.button1)

		splitter2 = QSplitter(Qt.Vertical)
		splitter2.addWidget(self.widgets)
		splitter2.addWidget(self.edit)
		splitter2.addWidget(self.splitter1)
		#splitter1.setGeometry(0, 0, 1500, 1500)

		hbox.addWidget(splitter2)
		self.setLayout(hbox)

	def doAddColumns(self):
		textbox = self.edit.toPlainText()
		Data = Convert_to_Column(textbox)
		if len(Data) == 1:
			projectes.add_Column(Data[0])
		elif len(Data) > 1:
			for i in range(len(Data)):
				projectes.add_Column(Data[i])
		GUI().refresh()

	def doChangeColumns(self):
		textbox = self.edit.toPlainText()
		Data = Convert_to_Column(textbox)
		if len(Data) == 1:
			print 'error'
		elif len(Data) > 1:
			projectes.change_Table(Data)
		GUI().refresh()

class MyTableWidget(QWidget):

	def __init__(self, parent, numtabses):
		super(QWidget, self).__init__(parent)
		self.layout = QVBoxLayout(self)
		self.splitters_widget = MySplitterWidget(self)

		self.tabs = QTabWidget()
		for i in range (1,numtabses+1):
			self.tabses(i)	

		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

	def tabses(self, numtabses):

		self.splitters_widget1 = MySplitterWidget(self)
		self.tab = self.splitters_widget1
		self.tabs.addTab(self.tab, "Tabla "+str(numtabses))

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print (currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class MyWidgets(QWidget):

	def __init__(self):
		super(MyWidgets, self).__init__()

		if "Hamilton" in projectes.get_Function():
			self.Hamil()
		if "calendar" in projectes.get_Function():
			self.calendar()
		if "progressbar" in projectes.get_Function():
			self.progressbar()
		if "checkBottom" in projectes.get_Function():
			self.checkBottom()
		if "graph" in projectes.get_Function():
			self.comboBox()
			#self.checkBox()
		if "Formulation" in projectes.get_Function():
			self.Formulation()
		if "Calculator" in projectes.get_Function():
			self.Errores()
		if "Nothing" in projectes.get_Function():
			None
		
		self.show()

	def Hamil(self):
		self.lbl1 = QLabel("<i>r<sub>0<\sub><\i>", self)
		self.lbl1.move(0, 51)
		self.textbox1 = QLineEdit(self)
		self.textbox1.move(50, 50)
		self.textbox1.resize(50,20)

		self.lbl2 = QLabel("<i>k<\i>", self)
		self.lbl2.move(120, 51)
		self.textbox2 = QLineEdit(self)
		self.textbox2.move(140, 50)
		self.textbox2.resize(50,20)

		self.lbl3 = QLabel("<i>l<sub>0<\sub><\i>", self)
		self.lbl3.move(200, 51)
		self.textbox3 = QLineEdit(self)
		self.textbox3.move(230, 50)
		self.textbox3.resize(50,20)

		self.lbl4 = QLabel("Masa/g", self)
		self.lbl4.move(0, 101)
		self.textbox4 = QLineEdit(self)
		self.textbox4.move(50, 100)
		self.textbox4.resize(50,20)

		self.lbl5 = QLabel(u'\u03B8', self)
		self.lbl5.move(120, 101)
		self.textbox5 = QLineEdit(self)
		self.textbox5.move(140, 100)
		self.textbox5.resize(50,20)

		self.lbl6 = QLabel("<i>V<sub>r<\sub><\i>", self)
		self.lbl6.move(200, 101)
		self.textbox6 = QLineEdit(self)
		self.textbox6.move(230, 100)
		self.textbox6.resize(50,20)

		self.lbl7 = QLabel("<i>V<sub>&theta;<\sub><\i>", self)
		self.lbl7.move(0, 151)
		self.textbox7 = QLineEdit(self)
		self.textbox7.move(50, 150)
		self.textbox7.resize(50,20)

		self.lbl8 = QLabel("<i>n<\i>", self)
		self.lbl8.move(120, 151)
		self.textbox8 = QLineEdit(self)
		self.textbox8.move(140, 150)
		self.textbox8.resize(50,20)

		self.lbl9 = QLabel("<i>dt<\i>", self)
		self.lbl9.move(200, 151)
		self.textbox9 = QLineEdit(self)
		self.textbox9.move(230, 150)
		self.textbox9.resize(50,20)

		self.button4 = QPushButton('Calculate', self)
		self.button4.move(220,180)

		# connect button to function on_click
		self.button4.clicked.connect(self.Rosberg)

	def Rosberg(self):
		m = float(self.textbox4.text())  
		k = float(self.textbox2.text())
		l0 = float(self.textbox3.text())
		r0 = float(self.textbox1.text())
		theta0 = float(self.textbox5.text())
		vr = float(self.textbox6.text())
		vtheta = float(self.textbox7.text())
		n = int(self.textbox8.text())
		dt = float(self.textbox9.text())

		hamilton = Hamilton(m, k, l0, r0, theta0, vr, vtheta, n, dt).get_file()
		projectes.change_Table(Open_file_CSV(hamilton).get_all())
		os.remove(hamilton)
		projectes.del_Function("Hamilton")		

	def Errores(self):
		self.lbl1 = QLabel("<i>Simbolos<\i>", self)
		self.lbl1.move(0, 51)
		self.textbox1 = QLineEdit(self)
		self.textbox1.move(60, 50)
		self.textbox1.resize(140,20)

		self.lbl4 = QLabel("<i>Valores<\i>", self)
		self.lbl4.move(0, 101)
		self.textbox4 = QLineEdit(self)
		self.textbox4.move(50, 100)
		self.textbox4.resize(150,20)

		self.lbl7 = QLabel("<i>Errores<\i>", self)
		self.lbl7.move(0, 151)
		self.textbox7 = QLineEdit(self)
		self.textbox7.move(50, 150)
		self.textbox7.resize(150,20)

		self.lbl8 = QLabel("<i>f = <\i>", self)
		self.lbl8.move(0, 201)
		self.textbox8 = QLineEdit(self)
		self.textbox8.move(30, 200)
		self.textbox8.resize(170,20)

		self.button4 = QPushButton('Calculate', self)
		self.button4.move(220,210)

		# connect button to function on_click
		self.button4.clicked.connect(self.CalculateErrors)

	def CalculateErrors(self):
		Simbolos = self.textbox1.text()
		valores = eval(self.textbox4.text())
		errores = eval(self.textbox7.text())
		funcion = str(self.textbox8.text())
		valorError = Errores(Simbolos, valores, errores, funcion).Errors()
		projectes.del_Function("Calculator")
		GUI().refresh()
		error = QMessageBox()
		error.setText(str(valorError))
		error.setWindowTitle('Error Calculator')
		window = error.exec_()

	def comboBox(self):
		self.lbl11 = QLabel("Graphics", self)
		self.lbl11.move(0, 480)

		self.lbl12 = QLabel("<h1>X</h1>", self)
		self.lbl12.move(60, 500)

		combo = QComboBox(self)
		combo.move(90, 500)
		for i in range(projectes.get_Len_Table()):
			combo.addItem(projectes.get_Table()[i].get_name())
		combo.activated[int].connect(self.onActivatedX)

		self.lbl13 = QLabel("<h1>Y</h1>", self)
		self.lbl13.move(60, 530)

		combo1 = QComboBox(self)
		combo1.move(90, 530)
		for i in range(projectes.get_Len_Table()):
			combo1.addItem(projectes.get_Table()[i].get_name())
		combo1.activated[int].connect(self.onActivatedY)

	"""def checkBox(self):
		cb = QCheckBox('Add Axis', self)
		cb.move(180, 500)
		cb.stateChanged.connect(self.addAxis)

	def addAxis(self, state):
		if state == Qt.Checked:
			combo2 = QComboBox(self)
			combo2.move(200, 530)
			for i in range(projectes.get_Len_Table()):
				combo2.addItem(projectes.get_Table()[i].get_name())
			combo2.activated[int].connect(self.onActivatedYPlus)
			self.show()"""

	def onActivatedX(self, text):
		projectes.get_Represent()[0] = text

	def onActivatedY(self, text):
		projectes.get_Represent()[1] = text

	def onActivatedYPlus(self, text):
		projectes.add_Represent(text)

	def Formulation(self):
		self.lbl14 = QLabel("Formula Entry", self)
		self.lbl14.move(10, 570)
		#self.onActivated("Formula Entry")
		self.textbox13 = QLineEdit(self)
		self.textbox13.move(20, 600)
		self.textbox13.resize(280,20)
		self.button3 = QPushButton('Run', self)
		self.button3.move(220,630)

		# connect button to function on_click
		self.button3.clicked.connect(self.on_click)

	@pyqtSlot()
	def on_click(self):
		textboxValue = self.textbox13.text()
		Inteface().formulating(textboxValue)
		GUI().refresh()

class PlotCanvas(FigureCanvas):

	def __init__(self, parent=None, width=5, height=4, dpi=100):
		self.fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = self.fig.add_subplot(111)

		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self,
				QSizePolicy.Expanding,
				QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

		self.functionGraph = Graphics(projectes.get_Table(), projectes.get_Represent())

		self.nameX = self.functionGraph.Names()[0]
		self.nameY = self.functionGraph.Names()[1]
		self.X = self.functionGraph.Values()[0]
		self.Y = self.functionGraph.Values()[1]

		self.Interval = self.functionGraph.IntervalLimits()

		try:
			if "Linear" in projectes.get_Function():
				self.plotLinear()
			elif "Logarithmic" in projectes.get_Function():
				self.plotLog()
			elif "Exponential" in projectes.get_Function():
				self.plotExp()
			elif "Sinusoidal" in projectes.get_Function():
				self.plotSin()
			elif "Polynomial" in projectes.get_Function():
				self.plotPoly()
			elif "Scratter" in projectes.get_Function():
				self.plotScratter()
			else:
				self.plotScratter()
		except (NameError, IndexError, ValueError, IOError, SyntaxError, TypeError):
			error = QMessageBox()
			error.setText("Error 99")
			error.setWindowTitle("Error 99")
			window = error.exec_()

	def plotSin(self):
		equation = self.functionGraph.sin_get_Ecuation()

		ax = self.figure.add_subplot(111)
		ax.plot(equation, 'r')
		ax.plot(self.X, self.Y, 'ro')
		ax.set_xlim(self.Interval[0])
		ax.set_ylim(self.Interval[1])
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def plotPoly(self):
		equation = self.functionGraph.Polget_Ecuacion(projectes.get_index())
		xes = equation[0]
		yes = equation[1]
		
		#data = [random.random() for i in range(25)]
		ax = self.figure.add_subplot(111)
		ax.plot(xes, yes, 'r', self.X, self.Y, 'ro')
		ax.set_xlim(self.Interval[0])
		ax.set_ylim(self.Interval[1])
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def plotScratter(self):
		ax = self.figure.add_subplot(111)
		if len(projectes.get_Represent()) == 2:
			ax.plot(self.X, self.Y, 'ro')
		elif len(projectes.get_Represent()) > 2:
			YY = projectes.get_Table()[projectes.get_Represent()[2]]
			ax.plot(self.X, self.Y, 'r', self.X, YY, 'bo')
		ax.set_xlim(self.Interval[0])
		ax.set_ylim(self.Interval[1])
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def plotLinear(self):
		equation = self.functionGraph.Linget_Ecuation()
		xes = equation[0]
		yes = equation[1]
		
		#data = [random.random() for i in range(25)]
		ax = self.figure.add_subplot(111)
		ax.plot(xes, yes, 'r', self.X, self.Y, 'ro')
		ax.set_xlim(self.Interval[0])
		ax.set_ylim(self.Interval[1])
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def plotLog(self):
		equation = self.functionGraph.Logget_Ecuation()
		xes = equation[0]
		yes = equation[1]

		ax = self.figure.add_subplot(111)
		ax.plot(xes, yes, 'r', self.X, self.Y, 'ro')
		ax.set_xlim(self.Interval[0])
		ax.set_ylim(self.Interval[1])
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def plotExp(self):
		equation = self.functionGraph.Expget_Ecuation()
		xes = equation[0]
		yes = equation[1]

		ax = self.figure.add_subplot(111)
		ax.plot(xes, yes, 'r', self.X, self.Y, 'ro')
		ax.set_xlim(self.Interval[0])
		ax.set_ylim(self.Interval[1])
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def savePlot(self):
		try:
			self.fig.savefig(projectes.get_Path()+projectes.get_Title())
		except IndexError:
			GUI().save()

class Inteface():

	def differential(self, text):
		projectes.add_Column(diff(projectes.get_Table()[text[0]], projectes.get_Table()[text[1]]))

	def details(self):
		functionGraph = Graphics(projectes.get_Table(), projectes.get_Represent())
		if "Linear" in projectes.get_Function():
			functionGraph.LinDetails()
		elif "Logarithmic" in projectes.get_Function():
			functionGraph.LogDetails()
		elif "Exponential" in projectes.get_Function():
			functionGraph.ExpDetails()
		elif "Polynomial" in projectes.get_Function():
			functionGraph.PolDetails(projectes.get_index())

	def openingFile(self, text):
		try:
			try:
				if text.index(".csv") >= 0:
					projectes.change_Table(Open_file_CSV(text).get_all())
			except ValueError:
				try:
					if text.index(".txt") >= 0:
						projectes.change_Table(Open_file_TXT(text).get_all())
				except ValueError:
					print 'Enable to open'
		except IOError:
			print 'Sorry that directory does not exist or no able to treated as file' # if it is not, print an error message

	def formulating(self, text):
		new_object = Operations(text, projectes.get_Table()).Returner()

		if new_object[2] >= projectes.get_Len_Table():
			projectes.add_Column(Variable(new_object[0], new_object[1]))
		else:
			if "Delete Column" == new_object[1]:
				projectes.delete_Column(new_object[2])
				projectes.set_Represent([None, None])

			else:
				projectes.change_Column(new_object[2], Variable(new_object[0], new_object[1]))

	def savingCSV(self, ):
		if projectes.get_Path() == None:
			raise IndexError
		else:
			try:
				if projectes.get_Path().index(".csv") >= 0:
					saveCSV(projectes.get_Path(), projectes.get_Table())
			except ValueError:
				try:
					if projectes.get_Path().index(".txt") >= 0:
						saveText(projectes.get_Path(), projectes.get_Table())
				except ValueError:
						print 'Enable to open'
		if not None in projectes.get_Represent():
				PlotCanvas().savePlot()

	def savingTex(self, path, text):
		if 'all' in text:
			allData = projectes.get_Table()
		else:
			text = eval(text)
			allData = [projectes.get_Table()[text[0]]]
			for i in range(1,len(text)):
				allData.append(projectes.get_Table()[text[i]])
		saveLaTex(path, allData)
		if not None in projectes.get_Represent():
			PlotCanvas().savePlot()

class Projects():
	""" """

	def __init__(self, Path, Title, Represent, Table, Function):
		self.Path = Path
		self.Title = Title
		self.Represent = Represent
		self.Table = Table
		self.Function = Function


	def set_index(self, index):
		self.index = index
	def get_index(self):
		return self.index
	def get_Path(self):
		return self.Path
	def set_Path(self, path):
		self.Path = path
	def get_Title(self):
		return self.Title
	def set_Title(self, title):
		self.Title = title
	def get_Represent(self):
		return self.Represent
	def set_Represent(self, represent):
		self.Represent = represent
	def add_Represent(self, represent):
		self.Represent.append(represent)
	def get_Table(self):
		return self.Table
	def get_Len_Table(self):
		return len(self.Table)
	def change_Table(self, Variables):
		self.Table = Variables
	def add_Column(self, Variable):
		self.Table.append(Variable)
	def change_Column(self, index, Variable):
		self.Table[index] = Variable
	def delete_Column(self, index):
		del self.Table[index]
	def get_Function(self):
		return self.Function
	def add_Function(self, function):
		self.Function.append(function)
	def del_Function(self, function):
		self.Function.remove(function)

try:
	if __name__ == '__main__':
		numtabses = 0
		projectes = Projects(None, None, [None, None], [], ["Nothing"])

		app = QApplication(sys.argv)
		ex = GUI()
		sys.exit(app.exec_())	
except (NameError, IndexError, ValueError, IOError, SyntaxError, TypeError):
	error = QMessageBox()
	error.setText("Error 99")
	error.setWindowTitle("Error 99")
	window = error.exec_()
