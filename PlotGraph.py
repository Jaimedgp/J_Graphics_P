#########################################
#              Main Window              #
#########################################
#
#   This class create the object with the interface required to 
#       represent and plot the graph using the package FigureCanvas.
#   This get the values to represent from the class GraphPlot in GraphPlot.py
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

        self.axes = self.fig.add_subplot(111)

    def setGraph(self, GraphPlot, marker='ro'):

        self.Graph = GraphPlot

        if marker == 'ro':
        	self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
        		               yerr=self.Graph.error, fmt=marker, ecolor='r')

        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, marker)
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_Hamil_Graph(self, GraphPlot):

        self.Graph = GraphPlot

        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'b')
        self.axes.set_xlabel(self.Graph.xTitle)
        self.axes.set_ylabel(self.Graph.yTitle)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_linearGraph(self, GraphPlot):

        self.Graph = GraphPlot

        slope, intercept = self.Graph.linearRegression()

        self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
        	               yerr=self.Graph.error, fmt='ro', ecolor='r')
      
        self.axes.plot(self.Graph.xTh, slope*self.Graph.xTh+intercept, 'b')
        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_logGraph(self, GraphPlot):

        from math import log

        self.Graph = GraphPlot

        slope, intercept = self.Graph.logarithmicRegression()

        yTh = [slope*log(self.Graph.xTh[i])+intercept for i in range(
        	                                             self.Graph.xTh.size)]

        self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
        	               yerr=self.Graph.error, fmt='ro', ecolor='r')

        self.axes.plot(self.Graph.xTh, yTh, 'b')
        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_expGraph(self, GraphPlot):

        from math import exp

        self.Graph = GraphPlot

        slope, intercept = self.Graph.exponentialRegression()
        yTh = [intercept*exp(slope*self.Graph.xTh[i]) for i in range(
        	                                              self.Graph.xTh.size)]     

        self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
        	               yerr=self.Graph.error, fmt='ro', ecolor='r')

        self.axes.plot(self.Graph.xTh, yTh, 'b')
        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_polyGraph(self, GraphPlot):

        from PyQt5.QtWidgets import QInputDialog, QFileDialog
        from numpy import poly1d

        self.Graph = GraphPlot

        text, ok = QInputDialog.getInt(self, 'Pepe adjust', 'Grade:')
        m = text

        parameters = self.Graph.polynomialRegression(m)

        polynom = poly1d(parameters)
        yTh = [polynom(self.Graph.xTh[i]) for i in range(self.Graph.xTh.size)]

        self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
        	yerr=self.Graph.error, fmt='ro', ecolor='r')
        self.axes.plot(self.Graph.xTh, yTh, 'b')
        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_PepepeGraph(self, GraphPlot):

        from PyQt5.QtWidgets import QInputDialog, QFileDialog

        self.Graph = GraphPlot

        text, ok = QInputDialog.getInt(self, 'Pepe adjust', 'Grade:')
        m = text

        fname = str(QFileDialog.getSaveFileName(self, 'Open file', 
        	                                          '/home/jaime/',
        	                                           "LaTex files (*.tex)"))

        fname = fname.split(',')[0]
        fname = fname.split('(u')
        fname = fname[1].split("'")

        slope, d = self.Graph.pepepe(m, fname[1])

        self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
        	               yerr=self.Graph.error, fmt='ro', ecolor='r')
        self.axes.plot(self.Graph.xTh, slope*(self.Graph.xTh**m), 'b')
        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def saveGraph(self):

        from PyQt5.QtWidgets import QFileDialog

        fileWindow = QFileDialog.getSaveFileName(self, 'Open file',
                                                       '/home/jaime/', 
                                                       "Image files (*.png)")

        fileWindow = str(fileWindow)
        fname = fileWindow.split(',')[0]
        fname = fname.split('(u')
        fname = fname[1].split("'")
        file = fname[1]

        self.fig.set_size_inches(9,6)
        self.fig.savefig(file, bbox_inches='tight')
