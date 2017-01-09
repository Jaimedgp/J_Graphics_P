"""
	JDG (Just a Graphics' Printer) 

	This program has been develop by Jaime Diez Gonzalez-Pardo in Python in 
	order to facilitate operations in performing laboratory practice

													Version: Enero 2017
"""

from PyQt5.QtWidgets import (QToolTip, QMessageBox, QDesktopWidget, QInputDialog, QHBoxLayout, QFrame, QSplitter, QStyleFactory, 
	QMainWindow, QTabWidget, QTextEdit, QAction, QApplication, QWidget, QFormLayout, QPushButton, QLineEdit, QTableWidget,
	QTableWidgetItem, QVBoxLayout, QFileDialog, QSizePolicy, QCalendarWidget, QLabel, QProgressBar, QCheckBox, QComboBox, QDoubleSpinBox, QGroupBox, QSpinBox)
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

		self.setGeometry(0, 0, 2000, 1100)
		self.setWindowTitle('Just a Graphics Printer')
		self.setWindowIcon(QIcon('./python_utilities/python_utilities_gui/JGP(icon).png'))

		self.Widget = Widgets()
		self.setCentralWidget(self.Widget)

		self.show()

	def menuBarsus(self):

		openAction = QAction('Open file', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open a table from a file')
		openAction.triggered.connect(self.openfile)

		saveAction = QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save table')
		saveAction.triggered.connect(self.saveCSV)

		saveAs = QAction('Save as', self)
		#saveAs.setShortcut('Ctrl+S')
		saveAs.setStatusTip('Save table')
		##saveAs.triggered.connect(self.saveAs)

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
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAs)
		fileMenu.addAction(saveTex)
		fileMenu.addAction(exitAction)

		Graph = QAction('Graphic', self)
		Graph.setShortcut('Ctrl+G')
		#Graph.setStatusTip('y = a*x + b')
		Graph.triggered.connect(self.graph)

		details = QAction('Show Details', self)
		#Graph.setShortcut('Ctrl+G')
		#Graph.setStatusTip('y = a*x + b')
		##details.triggered.connect(self.detail)

		Scrat = QAction('Scratter', self)
		#Scrat.setShortcut('Ctrl+G')
		#Graph.setStatusTip('y = a*x + b')
		##Scrat.triggered.connect(self.graph)

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

		generalGraph = QAction('fit 1', self)
		##generalGraph.triggered.connect(self.general)

		sinusoidalGraph = QAction('Sinusoidal', self)
		#sinusoidalGraph.setShortcut('Ctrl+S')
		#sinusoidalGraph.setStatusTip('b * e^(a*x)')
		##sinusoidalGraph.triggered.connect(self.sinusoidal)

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

		diffCalculator = QAction('Derivative', self)
		#diffCalculator.setShortcut('Ctrl+E')
		diffCalculator.setStatusTip('Calculate the derivative between two columns')
		#diffCalculator.triggered.connect(self.differential)

		refreshed = QAction('Refresh Window', self)
		refreshed.setShortcut('Ctrl+R')
		refreshed.triggered.connect(self.refresh)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Tools')
		fileMenu.addAction(diffCalculator)
		fileMenu.addAction(refreshed)

	def graph(self):
		Function["graph"] = True
		self.refresh()

	def linearing(self):
		Function["graph"] = True
		Function['type'] = "Linear"
		self.refresh()

	def exponential(self):
		Function["graph"] = True
		Function['type'] = "Exponential"
		self.refresh()

	def logarithmic(self):
		Function["graph"] = True
		Function['type'] = "Logarithmic"
		self.refresh()

	def polynomial(self):
		Function["graph"] = True
		Function['type'] = "Polynomial"
		self.refresh()

	def openfile(self):
		fileName = QFileDialog.getOpenFileName(self, 'Open file', '/home/jaime', 'Text File (*.csv *.txt)')

		Interface().openingFile(fileName[0])
		self.refresh()

	def differential(self):
		text, ok = QInputDialog.getText(self, 'Derivadas', '    Columns <h6>e.j."1,2" for columns C1 and C2<\h6>:')
		if ok:
			text = eval(text)
			Interface().differential(text)
		self.refresh()

	def saveCSV(self):
		try:
			Interface().savingCSV()
		except IndexError:
			fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Calc files (*.csv *.txt)"))
			fname = fname.split(',')[0]
			fname = fname.split('(u')
			fname = fname[1].split("'")
			projectes.set_Path(fname[1])
			Interface().savingCSV()

	def saveTex(self):
		text, ok = QInputDialog.getText(self, 'Export LaTex', '    Columns <h6>e.j."1,2" for columns C1 and C2<\h6> or "all" for all table:')
		if ok:
			fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "LaTex files (*.tex)"))
			fname = fname.split(',')[0]
			fname = fname.split('(u')
			fname = fname[1].split("'")
		Interface().savingTex(fname[1], text)

	def closeEvent(self, event):
		reply = QMessageBox.information(self, ' ', "Save changes before closing?", QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard, QMessageBox.Save)

		if reply == QMessageBox.Save:
			try:
				Interface().savingCSV()
			except IndexError:
				fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Calc files (*.csv *.txt)"))
				fname = fname.split(',')[0]
				fname = fname.split('(u')
				fname = fname[1].split("'")
				projectes.set_Path(fname[1])
				Interface().savingCSV()
			event.accept()
		elif reply == QMessageBox.Discard:
			event.accept()
		else:
			event.ignore()

	def refresh(self):
		self.Widget = Widgets()
		self.setCentralWidget(self.Widget)	

class Hamiltonian(QWidget):

	def __init__(self):
		super(QWidget, self).__init__()
		self.lbl1 = QLabel("<i>r<sub>0<\sub><\i>", self)
		self.textbox1 = QDoubleSpinBox(self)

		self.lbl2 = QLabel("<i>k<\i>", self)
		self.textbox2 = QDoubleSpinBox(self)

		self.lbl3 = QLabel("<i>l<sub>0<\sub><\i>", self)
		self.textbox3 = QDoubleSpinBox(self)

		self.lbl4 = QLabel("Masa/g", self)
		self.textbox4 = QDoubleSpinBox(self)

		self.lbl5 = QLabel(u'\u03B8', self)
		self.textbox5 = QDoubleSpinBox(self)

		self.lbl6 = QLabel("<i>V<sub>r<\sub><\i>", self)
		self.textbox6 = QDoubleSpinBox(self)

		self.lbl7 = QLabel("<i>V<sub>&theta;<\sub><\i>", self)
		self.textbox7 = QDoubleSpinBox(self)

		self.lbl8 = QLabel("<i>n<\i>", self)
		self.textbox8 = QDoubleSpinBox(self)

		self.lbl9 = QLabel("<i>dt<\i>", self)
		self.textbox9 = QDoubleSpinBox(self)

		self.button4 = QPushButton('Calculate', self)

		vbox = QVBoxLayout()
		vbox.addWidget(self.textbox9)
		vbox.addWidget(self.button4)

		fbox1 = QFormLayout()
		fbox1.addRow(self.lbl1, self.textbox1)
		fbox1.addRow(self.lbl4, self.textbox4)
		fbox1.addRow(self.lbl7, self.textbox7)

		fbox2 = QFormLayout()
		fbox2.addRow(self.lbl2, self.textbox2)
		fbox2.addRow(self.lbl5, self.textbox5)
		fbox2.addRow(self.lbl8, self.textbox8)

		fbox3 = QFormLayout()
		fbox3.addRow(self.lbl3, self.textbox3)
		fbox3.addRow(self.lbl6, self.textbox6)
		fbox3.addRow(self.lbl9, vbox)

		hbox = QHBoxLayout()
		hbox.addLayout(fbox1)
		hbox.addLayout(fbox2)
		hbox.addLayout(fbox3)

		self.setLayout(hbox)

		self.button4.clicked.connect(self.Rosberg)

	def Rosberg(self):
		m = self.textbox4.value()  
		k = self.textbox2.value()
		l0 = self.textbox3.value()
		r0 = self.textbox1.value()
		theta0 = self.textbox5.value()
		vr = self.textbox6.value()
		vtheta = self.textbox7.value()
		n = self.textbox8.value()
		dt = self.textbox9.value()

		hamilton = Hamilton(m, k, l0, r0, theta0, vr, vtheta, n, dt).get_file()
		projectes.change_Table(Open_file_CSV(hamilton).get_all())
		os.remove(hamilton)

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print (currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())	

class ErrorCalc(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()
		self.lbl1 = QLabel("<i>Simbolos<\i>", self)
		self.textbox1 = QLineEdit(self)

		self.lbl4 = QLabel("<i>Valores<\i>", self)
		self.textbox4 = QLineEdit(self)

		self.lbl7 = QLabel("<i>Errores<\i>", self)
		self.textbox7 = QLineEdit(self)

		self.lbl8 = QLabel("<i>f = <\i>", self)
		self.textbox8 = QLineEdit(self)

		hbox = QHBoxLayout()

		self.button4 = QPushButton('Calculate', self)
		# connect button to function on_click
		self.button4.clicked.connect(self.CalculateErrors)

		hbox.addWidget(self.button4)
		hbox.addStretch(1)
		vbox = QVBoxLayout()
		vbox.addWidget(self.textbox8)
		vbox.addLayout(hbox)

		fbox = QFormLayout()
		fbox.addRow(self.lbl1, self.textbox1)
		fbox.addRow(self.lbl4, self.textbox4)
		fbox.addRow(self.lbl7, self.textbox7)
		fbox.addRow(self.lbl8, vbox)

		self.setLayout(fbox)


	def CalculateErrors(self):
		Simbolos = self.textbox1.text()
		valores = eval(self.textbox4.text())
		errores = eval(self.textbox7.text())
		funcion = str(self.textbox8.text())
		valorError = Errores(Simbolos, valores, errores, funcion).Errors()
		ex.refresh()
		error = QMessageBox()
		error.setText(str(valorError))
		error.setWindowTitle('Error Calculator')
		window = error.exec_()

class Table(QWidget):

	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
			
		self.makingtable()

		self.tableWidget.move(0,0)

		# table selection change
		self.tableWidget.doubleClicked.connect(self.on_click)
		
		if Function["graph"] and not None in projectes.get_Represent():
			self.plot = PlotCanvas(self, width=5, height=4)

		hbox = QHBoxLayout(self)
	
		
		splitter1 = QSplitter(Qt.Vertical)
		splitter1.setGeometry(0, 0, 1500, 900)
		splitter1.addWidget(self.tableWidget)
			
		if Function["graph"] and not None in projectes.get_Represent():
			splitter1.addWidget(self.plot)
		
		hbox.addWidget(splitter1)
		self.setLayout(hbox)

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

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

	def onChanged(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize() 

class Widgets(QWidget):
	
	def __init__(self):
		super(QWidget,self).__init__()

		self.Table = QHBoxLayout()

		self.Graphics = QGroupBox()
		self.Graphics.setTitle("Graphics")

		self.Formulation = QGroupBox()
		self.Formulation.setTitle("Formula Entry")

		self.Datos = Table(self)
		
		self.tools = QVBoxLayout()

		self.Graph()
		self.Formula()
		self.tools.addWidget(self.Graphics)
		self.tools.addWidget(self.Formulation)
		self.Terminal()

		self.Table.addWidget(self.Datos, 25)
		self.Table.addLayout(self.tools, 7)
		self.Table.addStretch(1)

		self.setLayout(self.Table)		
		
	def Terminal(self):
		vbox = QVBoxLayout()
		hbox = QHBoxLayout()

		self.edit = QTextEdit()
		self.button1 = QPushButton('Add Columns', self)
		self.button1.clicked.connect(self.doAddColumns)
		self.button2 = QPushButton('New Table', self)
		self.button2.clicked.connect(self.doChangeColumns)

		hbox.addWidget(self.button1)
		hbox.addWidget(self.button2)

		vbox.addWidget(self.edit)
		vbox.addLayout(hbox)

		self.tools.addLayout(vbox, 1)

	def Graph(self):
	
		self.comboBox()
		fbox = QFormLayout()
		fbox.addRow(self.lbl12, self.combo)
		fbox.addRow(self.lbl13, self.combo1)

		self.tabses()
		self.Graphics.setLayout(fbox)
		self.tools.addStretch()

	def Formula(self):
		vbox = QVBoxLayout()
		hbox = QHBoxLayout()

		self.textbox13 = QLineEdit(self)
		self.button3 = QPushButton('Run', self)
		self.button3.clicked.connect(self.on_click)

		vbox.addWidget(self.textbox13)
		hbox.addWidget(self.button3)
		hbox.addStretch(1)
		vbox.addLayout(hbox)
		self.Formulation.setLayout(vbox)

	def comboBox(self):

		self.lbl12 = QLabel("<h1>X</h1>", self)

		self.lbl13 = QLabel("<h1>Y</h1>", self)

		self.combo = QComboBox(self)
		for i in range(projectes.get_Len_Table()):
			self.combo.addItem(projectes.get_Table()[i].get_name())
		self.combo.activated[int].connect(self.onActivatedX)

		self.combo1 = QComboBox(self)
		for i in range(projectes.get_Len_Table()):
			self.combo1.addItem(projectes.get_Table()[i].get_name())
		self.combo1.activated[int].connect(self.onActivatedY)

	def onActivatedX(self, text):
		projectes.get_Represent()[0] = text

	def onActivatedY(self, text):
		projectes.get_Represent()[1] = text

	def onActivatedYPlus(self, text):
		projectes.add_Represent(text)

	def tabses(self):
		Hamiltonial = Hamiltonian()
		Errors = ErrorCalc()
		Barrs = ErrorBars()
		self.tabs =QTabWidget()
		self.tabs.addTab(Hamiltonial, "Hamiltonian")
		self.tabs.addTab(Errors, "Errors")
		self.tabs.addTab(Barrs, "Bars error")
		self.tools.addWidget(self.tabs)

	def doAddColumns(self):
		textbox = self.edit.toPlainText()
		Data = Convert_to_Column(textbox)
		if len(Data) == 1:
			projectes.add_Column(Data[0])
		elif len(Data) > 1:
			for i in range(len(Data)):
				projectes.add_Column(Data[i])
		ex.refresh()

	def doChangeColumns(self):
		textbox = self.edit.toPlainText()
		Data = Convert_to_Column(textbox)
		if len(Data) == 1:
			print 'error'
		elif len(Data) > 1:
			projectes.change_Table(Data)
		ex.refresh()

	@pyqtSlot()
	def on_click(self):
		textboxValue = self.textbox13.text()
		Interface().formulating(textboxValue)
		ex.refresh()

class ErrorBars(QWidget):

	def __init__(self):
		super(QWidget, self).__init__()

		self.fbox = QHBoxLayout()
		
		self.Column()

		self.setLayout(self.fbox)

	def Column(self):
		combo1 = QComboBox(self)
		for i in range(projectes.get_Len_Table()):
			combo1.addItem(projectes.get_Table()[i].get_name())
		combo1.activated[int].connect(self.columnerror)

		self.fbox.addWidget(combo1)

	def columnerror(self, text):
		GraphError['values'] = projectes.get_Table()[text].get_list_values()
		GraphError['Error'] = True
		ex.refresh()

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

		self.nameX, self.nameY = self.functionGraph.Names()
		self.X,	self.Y = self.functionGraph.Values()
		self.IntervalX, self.IntervalY = self.functionGraph.IntervalLimits()

		try:
			if Function['type'] == None:
				self.plotScratter()
			else:
				self.plotFunction()
		except (NameError, IndexError, ValueError, IOError, SyntaxError, TypeError):
			error = QMessageBox()
			error.setText("Error 99")
			error.setWindowTitle("Error 99")
			window = error.exec_()

	def plotScratter(self):
		ax = self.figure.add_subplot(111)
		ax.plot(self.X, self.Y, 'ro')
		ax.set_xlim(self.IntervalX)
		ax.set_ylim(self.IntervalY)
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def plotFunction(self):
		
		if Function['type'] == "Linear":
			xes, yes = self.functionGraph.Linget_Ecuation()
		elif Function['type'] == "Logarithmic":
			xes, yes = self.functionGraph.Logget_Ecuation()
		elif Function['type'] == "Exponential":
			xes, yes = self.functionGraph.Expget_Ecuation()
		elif Function['type'] == "Polynomial":
			xes, yes = self.functionGraph.Polget_Ecuacion(projectes.get_index())

		ax = self.figure.add_subplot(111)
		if GraphError['Error']:
			ax.errorbar(self.X, self.Y, yerr=GraphError['values'], fmt='ro', ecolor='r')
		ax.plot(xes, yes, 'r', self.X, self.Y, 'ro')
		ax.set_xlim(self.IntervalX)
		ax.set_ylim(self.IntervalY)
		ax.set_xlabel(self.nameX)
		ax.set_ylabel(self.nameY)
		self.draw()

	def savePlot(self):
		try:
			archive = projectes.get_Path().replace(".csv", ".png")
			dpi = 172
			self.fig.savefig(archive, bbox_inches='tight')
		except IndexError:
			ex.save()

class Interface():

	def differential(self, text):
		projectes.add_Column(diff(projectes.get_Table()[text[0]], projectes.get_Table()[text[1]]))

	def details(self):
		functionGraph = Graphics(projectes.get_Table(), projectes.get_Represent())
		if Function["Linear"]:
			functionGraph.LinDetails()
		elif Function["Logarithmic"]:
			functionGraph.LogDetails()
		elif Function["Exponential"]:
			functionGraph.ExpDetails()
		elif Function["Polynomial"]:
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

	def __init__(self, Path, Represent, Table):
		self.Path = Path
		self.Represent = Represent
		self.Table = Table

	def set_index(self, index):
		self.index = index
	def get_index(self):
		return self.index
	def get_Path(self):
		return self.Path
	def set_Path(self, path):
		self.Path = path
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

if __name__ == '__main__':
	projectes = Projects(None, [None, None], [])
	Function = {"graph" : False,
				'type' : None}
	GraphError = {'Error': False, 'values' : None}
	app = QApplication(sys.argv)
	ex = GUI()
	sys.exit(app.exec_())	
