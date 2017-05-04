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

    def set_Hamil_Graph(self, GraphPlot):
        self.Graph = GraphPlot

        axes = self.fig.add_subplot(111)

        axes.clear()

        axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'b')
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
	
    def set_logGraph(self, GraphPlot):

        from math import log

        self.Graph = GraphPlot

        slope, intercept = self.Graph.logarithmicRegression()
        yTh = [slope*log(self.Graph.xTh[i])+intercept for i in range(self.Graph.xTh.size)]

        axes = self.fig.add_subplot(111)

        axes.clear()

        axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
        axes.plot(self.Graph.xTh, yTh, 'b')
        axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        axes.set_xlabel(self.Graph.xTitle)
        axes.set_ylabel(self.Graph.yTitle)
        axes.set_xlim(self.Graph.xInterval)
        axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_expGraph(self, GraphPlot):

        from math import exp

        self.Graph = GraphPlot

        slope, intercept = self.Graph.exponentialRegression()
        yTh = [intercept*exp(slope*self.Graph.xTh[i]) for i in range(self.Graph.xTh.size)]

        axes = self.fig.add_subplot(111)

        axes.clear()

        axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
        axes.plot(self.Graph.xTh, yTh, 'b')
        axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        axes.set_xlabel(self.Graph.xTitle)
        axes.set_ylabel(self.Graph.yTitle)
        axes.set_xlim(self.Graph.xInterval)
        axes.set_ylim(self.Graph.yInterval)
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

        axes = self.fig.add_subplot(111)

        axes.clear()

        axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
        axes.plot(self.Graph.xTh, yTh, 'b')
        axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'ro')
        axes.set_xlabel(self.Graph.xTitle)
        axes.set_ylabel(self.Graph.yTitle)
        axes.set_xlim(self.Graph.xInterval)
        axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_PepepeGraph(self, GraphPlot):

        from PyQt5.QtWidgets import QInputDialog, QFileDialog

        self.Graph = GraphPlot

        text, ok = QInputDialog.getInt(self, 'Pepe adjust', 'Grade:')
        m = text

        fname = str(QFileDialog.getSaveFileName(self, 'Open file', '/home/jaime/', "LaTex files (*.tex)"))
        fname = fname.split(',')[0]
        fname = fname.split('(u')
        fname = fname[1].split("'")

        slope, d = self.Graph.pepepe(m, fname[1])

        axes = self.fig.add_subplot(111)

        axes.clear()

        axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, yerr=self.Graph.error, fmt='ro', ecolor='r')
        axes.plot(self.Graph.xTh, slope*(self.Graph.xTh**m), 'b')
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