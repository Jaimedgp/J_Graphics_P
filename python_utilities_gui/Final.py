import sys
from PyQt5.QtWidgets import (QToolTip, QMessageBox, QDesktopWidget, QInputDialog, QHBoxLayout, QFrame, QSplitter, QStyleFactory, 
	QMainWindow, QTabWidget, QTextEdit, QAction, QApplication, QWidget, QFormLayout, QPushButton, QLineEdit, QTableWidget,
	QTableWidgetItem, QVBoxLayout, QFileDialog, QSizePolicy, QCalendarWidget, QLabel, QProgressBar, QCheckBox, QComboBox)
from PyQt5.QtGui import QFont, QIcon 
from PyQt5.QtCore import QCoreApplication, pyqtSlot, Qt, QDate, QBasicTimer
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os # import os Miscellaneous operating system interfaces
from JGP1 import *

class GUI(QMainWindow):

	def __init__(self, allData):
		super(GUI,self).__init__()

		self.allData = allData

		self.menuBarsus()

		self.setGeometry(0, 0, 1950, 1056)
		self.setWindowTitle('Just a Graphics Printer')
		self.setWindowIcon(QIcon('./Desktop/JGP(GUI)/JGP(icon).png'))

		self.function = ["Nothing", "comboBox"]

		self.splitters1_widget = MySplitterWidget1(self, self.function, self.allData)
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
		saveAction.triggered.connect(self.save)

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

		linearGraph = QAction('Linear', self)
		#newAction.setShortcut('Ctrl+N')
		linearGraph.setStatusTip('y = a*x + b')
		"""saveAction.triggered.connect(save(Path, Title))"""

		logGraph = QAction('Logarithmic', self)
		#openAction.setShortcut('Ctrl+O')
		logGraph.setStatusTip('a*log(x) + b')
		"""saveAction.triggered.connect(save(Path, Title))"""

		expGraph = QAction('Exponential', self)
		#saveAction.setShortcut('Ctrl+S')
		expGraph.setStatusTip('b * e^(a*x)')
		"""saveAction.triggered.connect(save(Path, Title))"""

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Curve Fit')
		fileMenu.addAction(Graph)
		fileMenu.addAction(linearGraph)
		fileMenu.addAction(logGraph)
		fileMenu.addAction(expGraph)

		formulaEntry = QAction('Formula Entry', self)
		formulaEntry.setShortcut('Ctrl+F')
		formulaEntry.setStatusTip('Operate between columns')
		formulaEntry.triggered.connect(self.formulaOperator)

		errorsCalculator = QAction('Error Calculator', self)
		errorsCalculator.setShortcut('Ctrl+C')
		errorsCalculator.setStatusTip('Calculate the error from an equation')
		"""saveAction.triggered.connect(save(Path, Title))"""

		refreshed = QAction('Refresh Window', self)
		refreshed.setShortcut('Ctrl+R')
		refreshed.triggered.connect(self.refresh)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Tools')
		fileMenu.addAction(formulaEntry)
		fileMenu.addAction(errorsCalculator)
		fileMenu.addAction(refreshed)

	def graph(self):
		self.function.append("graph")
		self.refresh()

	def save(self):
		saving = True
		while saving:
			try:
				Inteface(self.allData).saving()
				saving = False
			except IndexError:
				fname = str(QFileDialog.getExistingDirectory(self, 'Open file'))
				info.append('Sin titulo')
				info.append(fname+'/')

	def formulaOperator(self):

		self.function.append("Formulation")
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
		self.allData = 0

		self.refresh()

		self.show()

	def openfile(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/jaime')

		self.allData = Inteface(self.allData).openingFile(fname[0])

		self.refresh()

		self.show()

	def closeEvent(self, event):

		reply = QMessageBox.information(self, ' ', "Save changes before closing?", QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard, QMessageBox.Save)

		if reply == QMessageBox.Save:
			saving = True
			while saving:
				try:
					Inteface(self.allData).saving()
					saving = False
				except IndexError:
					fname = str(QFileDialog.getExistingDirectory(self, 'Open file'))
					info.append('Sin titulo')
					info.append(fname+'/')
			event.accept()
		elif reply == QMessageBox.Discard:
			event.accept()
		else:
			event.ignore()

	def refresh(self):
		self.splitters1_widget = MySplitterWidget1(self, self.function, self.allData)
		self.setCentralWidget(self.splitters1_widget)

class MySplitterWidget1(QWidget):

	def __init__(self, parent, function, allData):
		global numtabses
		super(QWidget, self).__init__()
		self.allData = allData

		self.function = function

		self.table_widget = MyTableWidget(self, numtabses, self.function, self.allData)
		self.widgets = OtherSplitterWidget(self.allData, self.function)
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

	def __init__(self, parent, allData, function):
		super(QWidget, self).__init__(parent)

		self.allData = allData
		self.function = function

		self.createTable()

		for i in range(len(function)):
			if function[i] == "graph":
				self.plot = PlotCanvas(self, width=5, height=4)
				break
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
			length = len(self.allData[0].get_list_values())

			for i in range(len(self.allData)-1):
				if len(self.allData[i].get_list_values()) < len(self.allData[i+1].get_list_values()):
					length = len(self.allData[i+1].get_list_values())

			# Create table
			self.tableWidget = QTableWidget()
			self.tableWidget.setRowCount(length)
			self.tableWidget.setColumnCount(len(self.allData))
			titles = "self.tableWidget.setHorizontalHeaderLabels((self.allData[0].get_name()"
			for i in range(1,len(self.allData)):
				titles += ", self.allData["+str(i)+"].get_name()"
			titles += "))"
			eval(titles)

			for n in range(len(self.allData)-1):
				for i in range(length):
					try:
						self.tableWidget.setItem(i,n, QTableWidgetItem(str(self.allData[n].get_values(i))))
					except IndexError:
						self.tableWidget.setItem(i,n, QTableWidgetItem(' '))
					try:
						self.tableWidget.setItem(i,n+1, QTableWidgetItem(str(self.allData[n+1].get_values(i))))
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
	def __init__(self, allData, function):
		super(QWidget, self).__init__()

		self.allData = allData
		self.function = function
		hbox = QHBoxLayout(self)

		self.widgets = MyWidgets(self.function, self.allData)
		self.edit = QTextEdit()
		self.edit.setGeometry(0,0,200,500)

		splitter1 = QSplitter(Qt.Vertical)
		splitter1.addWidget(self.widgets)
		splitter1.addWidget(self.edit)
		#splitter1.setGeometry(0, 0, 1500, 1500)

		hbox.addWidget(splitter1)
		self.setLayout(hbox)

class MyTableWidget(QWidget):

	def __init__(self, parent, numtabses, function, allData):
		super(QWidget, self).__init__(parent)
		self.function = function
		self.layout = QVBoxLayout(self)
		self.allData = allData
		self.splitters_widget = MySplitterWidget(self, self.allData, self.function)

		self.tabs = QTabWidget()
		for i in range (1,numtabses+1):
			self.tabses(i)	

		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

	def tabses(self, numtabses):

		self.splitters_widget1 = MySplitterWidget(self, self.allData, self.function)
		self.tab = self.splitters_widget1
		self.tabs.addTab(self.tab, "Tabla "+str(numtabses))

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print (currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class MyWidgets(QWidget):

	def __init__(self, function, allData):
		super(MyWidgets, self).__init__()
		self.allData = allData

		for i in range(len(function)):
			if function[i] == "calendar":
				self.calendar()
			elif function[i] == "progressbar":
				self.progressbar()
			elif function[i] == "checkBottom":
				self.checkBottom()
			elif function[i] == "comboBox":
				self.comboBox()
			elif function[i] == "Formulation":
				self.Formulation()
			elif function[i] == "Nothing":
				None
		
		self.show()

	def calendar(self):
		cal = QCalendarWidget(self)
		cal.setGridVisible(True)
		cal.move(0, 0)
		cal.clicked[QDate].connect(self.showDate)

		self.lbl = QLabel(self)
		date = cal.selectedDate()
		self.lbl.setText(date.toString())
		self.lbl.move(100, 160)

	def showDate(self, date):
		self.lbl.setText(date.toString())

	def progressbar(self):
		self.pbar = QProgressBar(self)
		self.pbar.setGeometry(30, 40, 200, 25)
		self.pbar.move(80, 260)

		self.btn = QPushButton('Start', self)
		self.btn.move(220, 300)
		self.btn.clicked.connect(self.doAction)

		self.timer = QBasicTimer()
		self.step = 0

	def timerEvent(self, e):
		if self.step >= 100:
			self.timer.stop()
			self.btn.setText('Finished')
			return

		self.step = self.step + 1
		self.pbar.setValue(self.step)

	def doAction(self):
		if self.timer.isActive():
			self.timer.stop()
			self.btn.setText('Start')
			GUI(self.allData).newproject()
		else:
			self.timer.start(100, self)
			self.btn.setText('Stop')
	"""
	def checkBottom(self):
		
		self.lbl = QLabel("X", self)
		self.lbl.move(20, 720)
		self.lbl1 = QLabel("Y", self)
		self.lbl1.move(70, 720)
		
		a1 = QCheckBox('', self)
		a1.move(20, 740)
		a1.toggle()
		a1.stateChanged.connect(self.value)
		
		a2 = QCheckBox(self.allData[0].get_name(), self)
		a2.move(70, 740)
		a2.toggle()
		a2.stateChanged.connect(self.value)
		
		b1 = QCheckBox('', self)
		b1.move(20, 760)
		b1.toggle()
		b1.stateChanged.connect(self.value)
		
		b2 = QCheckBox(self.allData[1].get_name(), self)
		b2.move(70, 760)
		b2.toggle()
		b2.stateChanged.connect(self.value)

	def value(self, state):

		if state == Qt.Checked:
			print 'Hello'	
	"""
	def comboBox(self):
		self.lbl = QLabel("Graphics", self)
		self.lbl.move(0, 480)

		self.lbl = QLabel("<h1>X</h1>", self)
		self.lbl.move(100, 500)

		combo = QComboBox(self)
		combo.move(130, 500)
		for i in range(len(self.allData)):
			combo.addItem(self.allData[i].get_name())
		combo.activated[int].connect(self.onActivatedX)

		self.lbl1 = QLabel("<h1>Y</h1>", self)
		self.lbl1.move(100, 530)

		combo1 = QComboBox(self)
		combo1.move(130, 530)
		for i in range(len(self.allData)):
			combo1.addItem(self.allData[i].get_name())
		combo1.activated[int].connect(self.onActivatedY)

	def onActivatedX(self, text):
		graph[0] = text 

	def onActivatedY(self, text):
		graph[1] = text 

	def Formulation(self):
		self.lbl = QLabel("Formula Entry", self)
		self.lbl.move(10, 570)
		#self.onActivated("Formula Entry")
		self.textbox = QLineEdit(self)
		self.textbox.move(20, 600)
		self.textbox.resize(280,20)
		self.button = QPushButton('Run', self)
		self.button.move(220,630)

		# connect button to function on_click
		self.button.clicked.connect(self.on_click)

	@pyqtSlot()
	def on_click(self):
		textboxValue = self.textbox.text()
		Inteface(self.allData).formulating(textboxValue)
		GUI(self.allData).refresh()

class PlotCanvas(FigureCanvas):

	def __init__(self, parent=None, width=5, height=4, dpi=100):
		global graph, allData
		self.allData = allData
		self.fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = self.fig.add_subplot(111)

		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self,
				QSizePolicy.Expanding,
				QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.plot(graph)

	def plot(self, graph):
		x = graph[0]
		y = graph[1]
		X = self.allData[x].get_list_values()
		Y = self.allData[y].get_list_values()

		i = 1
		intervalY = Y[i]-Y[i-1]
		while intervalY == 0:
			i += 1
			intervalY = Y[i]-Y[i-1]
		i = 1
		intervalX = X[i]-X[i-1]
		while intervalX == 0:
			i += 1
			intervalX = X[i]-X[i-1]

		maxy = max(Y) + fabs(intervalY)*0.5 # Max value for y axis 
		miny = min(Y) - fabs(intervalY)*0.5 # Min value for y axis
		maxx = max(X) + fabs(intervalX)*0.5 # max value for x axis
		minx = min(X) - fabs(intervalX)*0.5 # min value for x axis
		#data = [random.random() for i in range(25)]
		ax = self.figure.add_subplot(111)
		ax.plot(X, Y, 'ro')
		ax.set_xlim([minx, maxx])
		ax.set_ylim([miny, maxy])
		ax.set_xlabel(self.allData[x].get_name())
		ax.set_ylabel(self.allData[y].get_name())
		self.draw()

	def savePlot(self):
		try:
			self.fig.savefig(info[1]+info[0])
		except IndexError:
			GUI(self.allData).save()

class Inteface():

	def __init__(self, allData):
		self.allData = allData

	def openingFile(self, text):
		try:
			self.allData = Open_file(text).get_all()
		except IOError:
			print 'Sorry that directory does not exist or no able to treated as file' # if it is not, print an error message
		return self.allData

	def formulating(self, text):
		new_object = Operations(text, self.allData).Returner()

		if new_object[2] >= len(self.allData):
			self.allData.append(Variable(new_object[0], new_object[1]))
		else:
			self.allData[new_object[2]] = Variable(new_object[0], new_object[1])
		GUI(self.allData).refresh()

	def saving(self):
		save(info[1], info[0], self.allData)
		PlotCanvas().savePlot()

if __name__ == '__main__':
	numtabses = 0
	info = []
	graph = [0,1]
	name = 'Distancia/m'
	values = [1,2,3,4,5,6,7,8,9,10]
	name1 = 'Tiempo/s'
	values1 = [1,2,3,4,5,6,7,8,9,10]
	allData = [Variable(name,values), Variable(name1,values1)]

	app = QApplication(sys.argv)
	ex = GUI(allData)
	sys.exit(app.exec_())	