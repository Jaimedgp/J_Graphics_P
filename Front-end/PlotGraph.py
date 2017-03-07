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
		self.axes = self.fig.add_subplot(111)

		FigureCanvas.__init__(self, self.fig)
		self.setParent(None)

		FigureCanvas.setSizePolicy(self,
				QSizePolicy.Expanding,
				QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def setGraph(self, GraphPlot):
		self.Graph = GraphPlot
