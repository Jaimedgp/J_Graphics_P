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
        #self.Terminal.pColButton.clicked.connect(self.addColumns)
        #self.Terminal.nwTblButton.clicked.connect(self.changeColumns)

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

    def plotGraph(self):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , self.dataTable.table[axesYTitle] ]
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            try:
                error = eval(self.ErrBar.Error[types].text())
            except AttributeError:
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        try:
            self.Graph.setGraph(graph)
        except AttributeError:
            self.Graph = Plot_Graph()

        self.Graph.setGraph(graph)
        self.splitLyout.addWidget(self.Graph)

    def plotLinearGraph(self):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , self.dataTable.table[axesYTitle] ]
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            try:
                error = eval(self.ErrBar.Error[types].text())
            except AttributeError:
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        try:
            self.Graph.set_linearGraph(graph)
        except AttributeError:
            self.Graph = Plot_Graph()
            self.Graph.set_linearGraph(graph)

        self.GrphAxes.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.GrphAxes.result.setText(graph.text)

        self.splitLyout.addWidget(self.Graph)

    def plotLogGraph(self):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , self.dataTable.table[axesYTitle] ]
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            try:
                error = eval(self.ErrBar.Error[types].text())
            except AttributeError:
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        try:
            self.Graph.set_logGraph(graph)
        except AttributeError:
            self.Graph = Plot_Graph()
            self.Graph.set_logGraph(graph)

        self.GrphAxes.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.GrphAxes.result.setText(graph.text)

        self.splitLyout.addWidget(self.Graph)

    def plotExpGraph(self):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , self.dataTable.table[axesYTitle] ]
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            try:
                error = eval(self.ErrBar.Error[types].text())
            except AttributeError:
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        try:
            self.Graph.set_expGraph(graph)
        except AttributeError:
            self.Graph = Plot_Graph()
            self.Graph.set_expGraph(graph)

        self.GrphAxes.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.GrphAxes.result.setText(graph.text)

        self.splitLyout.addWidget(self.Graph)

    def plotPolyGraph(self):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , self.dataTable.table[axesYTitle] ]
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            try:
                error = eval(self.ErrBar.Error[types].text())
            except AttributeError:
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        try:
            self.Graph.set_polyGraph(graph)
        except AttributeError:
            self.Graph = Plot_Graph()
            self.Graph.set_polyGraph(graph)

        self.GrphAxes.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.GrphAxes.result.setText(graph.text)

        self.splitLyout.addWidget(self.Graph)

    def plotPepeGraph(self):

        axesXTitle = self.GrphAxes.axesXCombo.currentText()
        axesYTitle = self.GrphAxes.axesYCombo.currentText()

        values = [ self.dataTable.table[axesXTitle] , self.dataTable.table[axesYTitle] ]
        titles = [ axesXTitle , axesYTitle ]

        types = self.ErrBar.MainCombo.currentText()
        if types != 'None':
            try:
                error = eval(self.ErrBar.Error[types].text())
            except AttributeError:
                error = self.ErrBar.Error[types].currentText()
                error = self.dataTable.table[error]
            graph = GraphPlot(values, titles, error)
        else:
            graph = GraphPlot(values, titles)

        try:
            self.Graph.set_PepepeGraph(graph)
        except AttributeError:
            self.Graph = Plot_Graph()
            self.Graph.set_PepepeGraph(graph)

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
                        if item.row() >= len(self.dataTable.table[self.dataTable.index[item.column()]]):
                            self.dataTable.table[self.dataTable.index[item.column()]]
                        else:
                            del self.dataTable.table[self.dataTable.index[item.column()]][item.row()]
                        boolean = False
                    else:
                        self.dataTable.table[self.dataTable.index[item.column()]][item.row()] = float(item.text())
                        boolean = False
                except IndexError:
                    self.dataTable.table[self.dataTable.index[item.column()]].append(float(item.text()))
                    boolean = False
                except KeyError:
                    self.dataTable.table[str(item.column())] = []
                    self.dataTable.index[item.column()] = str(item.column())
                    self.ErrBar.set_new_Columns_names(self.dataTable.index)
                    self.GrphAxes.setNames(self.dataTable.index)

    @pyqtSlot()
    def formula_click(self):

        table, index = Operations( self.Formula.lineEdit.text(), self.dataTable.table, self.dataTable.index ).main()

        self.dataTable.table = table
        self.dataTable.index = index
        self.dataTable.reDoTable()
        self.ErrBar.set_new_Columns_names(self.dataTable.index)
        self.GrphAxes.setNames(self.dataTable.index)
