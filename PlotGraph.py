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

from PyQt5.QtWidgets import QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Plot_Graph(FigureCanvas):

	def __init__(self):

		self.fig = Figure(figsize=(5, 4), dpi=100)
		

		FigureCanvas.__init__(self, self.fig)
		self.setParent(None)

		FigureCanvas.setSizePolicy(self,
				QSizePolicy.Expanding,
				QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def setGraph(self, GraphPlot):
		self.Graph = GraphPlot

		axes = self.fig.add_subplot(111)

		axes.clear()

		axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
		axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
		axes.set_xlabel(self.Graph.xTitle)
		axes.set_ylabel(self.Graph.yTitle)
		axes.set_xlim(self.Graph.xInterval)
		axes.set_ylim(self.Graph.yInterval)
		self.draw()

	def set_linearGraph(self, GraphPlot):

		self.Graph = GraphPlot

		slope, intercept = self.Graph.linearRegression()

		axes = self.fig.add_subplot(111)

		axes.clear()

		axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
		axes.plot(self.Graph.xTh, slope*self.Graph.xTh+intercept, 'b')
		axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
		axes.set_xlabel(self.Graph.xTitle)
		axes.set_ylabel(self.Graph.yTitle)
		axes.set_xlim(self.Graph.xInterval)
		axes.set_ylim(self.Graph.yInterval)
		self.draw()


	def set_PepepeGraph(self, GraphPlot):

		self.Graph = GraphPlot

		slope, d = self.Graph.pepepe(-1, '/home/jaime/pepepe.tex')

		axes = self.fig.add_subplot(111)

		axes.clear()

		axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
		axes.plot(self.Graph.xTh, slope*self.Graph.xTh**1, 'b')
		axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
		axes.set_xlabel(self.Graph.xTitle)
		axes.set_ylabel(self.Graph.yTitle)
		axes.set_xlim(self.Graph.xInterval)
		axes.set_ylim(self.Graph.yInterval)
		self.draw()

	def saveGraph(self):

		from PyQt5.QtWidgets import QFileDialog

		fileWindow = QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "Image files (*.png)")

		fileWindow = str(fileWindow)
		fname = fileWindow.split(',')[0]
		fname = fname.split('(u')
		fname = fname[1].split("'")
		file = fname[1]

		dpi = 172
		self.fig.savefig(file, bbox_inches='tight')