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
        self.color = ['r', 'b']
        self.nc = 0 #graph color index 

    def setGraph(self, GraphPlot, marker='o'):

        self.Graph = GraphPlot

        if marker == 'o':
            self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
                    yerr=self.Graph.error, fmt=self.color[self.nc]+marker, ecolor=self.color[self.nc])

        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, self.color[self.nc]+marker)
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

    def set_Regression(self, GraphPlot, types):

        self.Graph = GraphPlot

        if types=='lin':
            slope, intercept = self.Graph.linearRegression()
            yTh = [slope*self.Graph.xTh[i]+intercept for i in range(
                                                         self.Graph.xTh.size)]
        
        elif types=='log':
            from math import log

            slope, intercept = self.Graph.logarithmicRegression()
            yTh = [slope*log(self.Graph.xTh[i])+intercept for i in range(self.Graph.xTh.size)]
            
        elif types=='exp':
            from math import exp

            slope, intercept = self.Graph.exponentialRegression()
            yTh = [intercept*exp(slope*self.Graph.xTh[i]) for i in range(
                                                          self.Graph.xTh.size)]
        
        elif types == 'poly':
            from PyQt5.QtWidgets import QInputDialog, QFileDialog
            from numpy import poly1d

            self.Graph = GraphPlot

            text, ok = QInputDialog.getInt(self, 'Polynomial', 'Grade:')
            m = text

            parameters = self.Graph.polynomialRegression(m)

            polynom = poly1d(parameters)
            yTh = [polynom(self.Graph.xTh[i]) for i in range(self.Graph.xTh.size)]

        elif types == 'pepe':
            from PyQt5.QtWidgets import QInputDialog, QFileDialog

            self.Graph = GraphPlot

            text, ok = QInputDialog.getInt(self, 'Pepe adjust', 'Grade:')
            if ok:
                m = text
            else:
                return False

            fname, ok = QFileDialog.getSaveFileName(self, 'Open file', 
                                                          '/home/jaime/',
                                                           "LaTex files (*.tex)")

            if fname == '':
                return False

            fname = str(fname)

            slope, d = self.Graph.pepepe(m, fname)
            yTh = [slope*(self.Graph.xTh**m) for i in range(
                                                           self.Graph.xTh.size)]

        elif types == 'general':
            from PyQt5.QtWidgets import QInputDialog, QFileDialog
            import numpy as np

            self.Graph = GraphPlot

            text, ok = QInputDialog.getText(self, 'Curve Fit', 'Function:', text="t[0] * np.sin(t[1]*x + t[2]) + t[3] ; [1,1,1,1]")
            if ok:
                func, parameters = text.split(";")
            else:
                return False

            parameters = eval(parameters)

            t = self.Graph.generalFit(parameters, func)
            func = func.replace('x', 'self.Graph.xTh')
            yTh = eval(func)

        self.axes.errorbar(self.Graph.xAxis, self.Graph.yAxis, 
                           yerr=self.Graph.error, fmt=self.color[self.nc]+'o', ecolor=self.color[self.nc])
      
        self.axes.plot(self.Graph.xTh, yTh, self.color[self.nc])
        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, self.color[self.nc]+'o')
        self.axes.set_xlabel(self.Graph.xTitle, fontsize=20)
        self.axes.set_ylabel(self.Graph.yTitle, fontsize=20)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()

        return True

    def saveGraph(self):

        from PyQt5.QtWidgets import QFileDialog

        file, ok = QFileDialog.getSaveFileName(self, 'Open file',
                                                       '/home/jaime/', 
                                                       "Image files (*.png)")

        if ok:

            file = str(file)

            self.fig.set_size_inches(9,6)
            self.fig.savefig(file, bbox_inches='tight')

    def set_Hamil_Graph(self, GraphPlot):

        self.Graph = GraphPlot

        self.axes.plot(self.Graph.xAxis, self.Graph.yAxis, 'b')
        self.axes.set_xlabel(self.Graph.xTitle)
        self.axes.set_ylabel(self.Graph.yTitle)
        self.axes.set_xlim(self.Graph.xInterval)
        self.axes.set_ylim(self.Graph.yInterval)
        self.draw()
