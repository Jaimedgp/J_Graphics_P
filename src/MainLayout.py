from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QVBoxLayout, QGroupBox, QPushButton, QLineEdit, QTabWidget, QLabel, QComboBox, QFormLayout
from PyQt5.QtCore import pyqtSlot, Qt

from TableGUI import TableData
from PlotGraph import Plot_Graph
from GraphPlot import GraphPlot
from ToolsWidgets import *

from Calculator import Operations

class MainLayout(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        self.path = '/'

        self.MainLyout = QHBoxLayout()

        dataLyout = QHBoxLayout()
        self.widgetsLyout = QVBoxLayout()

        self.dataTable = TableData()
        self.dataTable.tableWidget.itemChanged.connect(self.changeData)

        self.ErrBar = ErrorBars()
        self.Hamiltonian = Hamiltonian()
        self.CalcError = CalculateError()
        self.GrphAxes = GraphAxes()
        self.Formula = FormulaEntry()
        self.Formula.runButton.clicked.connect(self.formula_click)
        self.Terminal = Terminal_for_table()

        toolsTab = QTabWidget()
        toolsTab.addTab(self.ErrBar, "Error Bars")
        toolsTab.addTab(self.Hamiltonian, "Hamiltonian")
        toolsTab.addTab(self.CalcError, "Errors")

        self.widgetsLyout.addWidget(toolsTab)
        self.widgetsLyout.addWidget(self.GrphAxes)
        self.widgetsLyout.addWidget(self.Formula)
        self.widgetsLyout.addWidget(self.Terminal)

        self.splitLyout = QSplitter(Qt.Vertical)
        self.splitLyout.setGeometry(0, 0, 1500, 1000)
        self.splitLyout.addWidget(self.dataTable.tableWidget)
        dataLyout.addWidget(self.splitLyout)

        self.MainLyout.addLayout(dataLyout, 25)
        self.MainLyout.addLayout(self.widgetsLyout, 7)

        self.dataSaved = True

        self.setLayout(self.MainLyout)

    def plotGraph(self, marker):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , 
                   self.dataTable.table[axesYTitle] ]

        if len(values[0]) != len(values[1]):
            return
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            if types == 'Fixed value':
                error = eval(self.ErrBar.Error[types].text())
            elif types == '% of value':
                percent = eval(self.ErrBar.Error[types].text())
                error = [(percent*0.01)*y for y in values[1]]
            elif types == 'Data column':
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        if not hasattr(self, 'Graph'):
           self.Graph = Plot_Graph()

        if not self.GrphAxes.checkReplot.isChecked():
            self.Graph.axes.clear()
            self.GrphAxes.result.setText('')
            self.Graph.nc = -1

        self.Graph.nc = self.Graph.nc + 1
        if self.Graph.nc >= len(self.Graph.color):
            self.Graph.nc = 0

        logX, logY = False, False

        if self.GrphAxes.checkLogAxsX.isChecked():
            logX = True
        if self.GrphAxes.checkLogAxsY.isChecked():
            logY = True

        self.Graph.setGraph(graph, marker, logX, logY)
        self.splitLyout.addWidget(self.Graph)

    def plotRegressionGraph(self, typof):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] ,
                   self.dataTable.table[axesYTitle] ]

        if len(values[0]) != len(values[1]):
            return
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            if types == 'Fixed value':
                error = eval(self.ErrBar.Error[types].text())
            elif types == '% of value':
                percent = eval(self.ErrBar.Error[types].text())
                error = [(percent*0.01)*y for y in values[1]]
            elif types == 'Data column':
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        if not hasattr(self, 'Graph'):
           self.Graph = Plot_Graph()

        if not self.GrphAxes.checkReplot.isChecked():
            self.Graph.axes.clear()
            self.GrphAxes.result.setText('')
            self.Graph.nc = -1
        else:
            if graph.xInterval[0] > self.Graph.axes.get_xlim()[0]:
                graph.xInterval[0] = self.Graph.axes.get_xlim()[0]
            if graph.xInterval[1] < self.Graph.axes.get_xlim()[1]:
                graph.xInterval[1] = self.Graph.axes.get_xlim()[1]
            if graph.yInterval[0] > self.Graph.axes.get_ylim()[0]:
                graph.yInterval[0] = self.Graph.axes.get_ylim()[0]
            if graph.yInterval[1] < self.Graph.axes.get_ylim()[1]:
                graph.yInterval[1] = self.Graph.axes.get_ylim()[1]


        self.Graph.nc = self.Graph.nc + 1
        if self.Graph.nc >= len(self.Graph.color):
            self.Graph.nc = 0


        if typof == 'lin':
            correct = self.Graph.set_Regression(graph, 'lin')
        elif typof == 'log':
            correct = self.Graph.set_Regression(graph, 'log')
        elif typof == 'exp':
            correct = self.Graph.set_Regression(graph, 'exp')
        elif typof == 'poly':
            correct = self.Graph.set_Regression(graph, 'poly')
        elif typof == 'pepe':
            correct = self.Graph.set_Regression(graph, 'pepe')
        elif typof == 'general':
            correct = self.Graph.set_Regression(graph, 'general')

        if correct:
            self.GrphAxes.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.GrphAxes.result.setText(graph.text)

            self.splitLyout.addWidget(self.Graph)

    def saveGraph(self):

        self.Graph.saveGraph()

    @pyqtSlot()
    def changeData(self):

        self.dataSaved = False

        for item in self.dataTable.tableWidget.selectedItems():
            boolean = True
            while boolean:
                try:
                    if item.text() == '':                   	
                        if item.row() >= len(self.dataTable.table[
                        	            self.dataTable.index[item.column()]]):

                            self.dataTable.table[self.dataTable.index[
                                                               item.column()]]
                        else:
                            del self.dataTable.table[self.dataTable.index[
                                                   item.column()]][item.row()]
                        boolean = False
                    else:
                        self.dataTable.table[self.dataTable.index[
                              item.column()]][item.row()] = float(item.text())
                        boolean = False
                except IndexError:
                    self.dataTable.table[self.dataTable.index[item.column()]
                                                  ].append(float(item.text()))
                    boolean = False
                except KeyError:
                    self.dataTable.table[str(item.column())] = []
                    self.dataTable.index[item.column()] = str(item.column())
                    self.ErrBar.set_new_Columns_names(self.dataTable.index)
                    self.GrphAxes.setNames(self.dataTable.index)

        self.dataTable.addColumnRow()

    @pyqtSlot()
    def formula_click(self):

        table, index = Operations( self.Formula.lineEdit.text(),
                                   self.dataTable.table, 
                                   self.dataTable.index ).main()

        self.dataTable.table = table
        self.dataTable.index = index
        self.dataTable.reDoTable()
        self.ErrBar.set_new_Columns_names(self.dataTable.index)
        self.GrphAxes.setNames(self.dataTable.index)
