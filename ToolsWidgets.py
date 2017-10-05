from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QGroupBox, QComboBox, QTextEdit
from PyQt5.QtCore import Qt


#########################################
#         Calculate the Error           #
#########################################
#
#   This class create the object with the interface
#       required to request the values to calculate the Error 
#       with the function ErrorsCalculator from WidgetsScript
#
#   Required: - symbols \ Line Edit \ "Symbol Symbol"
#             - variables' values \ Line Edit \ "float, float"
#             - variables' error's values \ Line Edit \  "float, float"
#             - function \ Line Edit \ str(function)
#
#   On_click: CalculateErrors set a label with the result
#
#########################################################################

class CalculateError(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        symbLabl = QLabel("<i>Variables<\i>", self)
        self.symbInput = QLineEdit(self)

        valsLabl = QLabel("<i>Values<\i>", self)
        self.valsInput = QLineEdit(self)

        errLabl = QLabel("<i>Errors<\i>", self)
        self.errInput = QLineEdit(self)

        funcLabl = QLabel("<i>f = <\i>", self)
        self.funcInput = QLineEdit(self)

        calcButton = QPushButton('Calculate', self)
        calcButton.clicked.connect(self.CalculateErrors)

        hbox = QHBoxLayout()
        hbox.addWidget(calcButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.funcInput)
        vbox.addLayout(hbox)

        fbox = QFormLayout()
        fbox.addRow(symbLabl, self.symbInput)
        fbox.addRow(valsLabl, self.valsInput)
        fbox.addRow(errLabl, self.errInput)
        fbox.addRow(funcLabl, vbox)

        labelbox = QHBoxLayout()
        self.result = QLabel('', self)
        labelbox.addWidget(self.result)

        VMainBox = QVBoxLayout()
        VMainBox.addLayout(fbox)
        VMainBox.addLayout(labelbox)

        self.setLayout(VMainBox)


    def CalculateErrors(self):

        from WidgetsScript import ErrorsCalculator

        symbol = self.symbInput.text()
        values = eval(self.valsInput.text())
        errors = eval(self.errInput.text())
        function = str(self.funcInput.text())

        valuError = ErrorsCalculator(symbol, values, errors, function)

        self.result.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.result.setText(str(valuError))


#########################################
#              Error Bars               #
#########################################
#
#   This class create the object with the interface
#       required to request the value/s of the graph's y-Axis 
#   This object allows to set the error by a column's values, 
#       percentage or a fixed value.
#
################################################################

class ErrorBars(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        self.VBox = QVBoxLayout()
        self.set_Error_By_Column()
        self.set_Error_By_Fixed()
        self.set_Error_By_Percent()

        hBox = QHBoxLayout()

        # Combo box to choose the error's type
        self.MainCombo = QComboBox(self)
        self.MainCombo.addItem("None")
        self.MainCombo.addItem("% of value")
        self.MainCombo.addItem("Fixed value")
        self.MainCombo.addItem("Data column")
        hBox.addWidget(self.MainCombo)

        VMainBox = QVBoxLayout()
        hBox.addLayout(self.VBox)
        VMainBox.addLayout(hBox)

        self.Error = {"% of value":self.percenValue, "Fixed value":self.value,
                                                  "Data column":self.errColumn}

        self.setLayout(VMainBox)

    def set_Error_By_Column(self):

        column = QGroupBox()
        column.setTitle('Data Column')

        vbox = QVBoxLayout()

        self.errColumn = QComboBox(self)

        vbox.addWidget(self.errColumn)
        column.setLayout(vbox)
        self.VBox.addWidget(column)

    def set_new_Columns_names(self, index):

        self.errColumn.clear()
        for name in index.values():
            self.errColumn.addItem(name)

    def set_Error_By_Fixed(self):

        Fixed = QGroupBox()
        Fixed.setTitle('Fixed value')

        vbox = QVBoxLayout()
        self.value = QLineEdit()
        vbox.addWidget(self.value)
        Fixed.setLayout(vbox)

        self.VBox.addWidget(Fixed)

    def set_Error_By_Percent(self):

        Percent = QGroupBox()
        Percent.setTitle('% of value')

        vbox = QVBoxLayout()
        self.percenValue = QLineEdit()
        vbox.addWidget(self.percenValue)
        Percent.setLayout(vbox)

        self.VBox.addWidget(Percent)


#########################################
#              Hamiltonian              #
#########################################
#
#   This class create the object with the interface
#       required to request the values to calculate the hamiltonian
#       with the function Hamiltonian from WidgetsScript
#
#   Required: 
#
#   Return: 
#
##############################################################################

class Hamiltonian(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        r0Labl = QLabel("<i>r<sub>0<\sub><\i>", self)
        self.r0Input = QLineEdit(self)

        kLabl = QLabel("<i>k<\i>", self)
        self.kInput = QLineEdit(self)

        l0labl = QLabel("<i>l<sub>0<\sub><\i>", self)
        self.l0Input = QLineEdit(self)

        mLabl = QLabel("Masa/g", self)
        self.mInput = QLineEdit(self)

        thetaLabl = QLabel(u'\u03B8', self)
        self.thetaInput = QLineEdit(self)

        vrLabl = QLabel("<i>V<sub>r<\sub><\i>", self)
        self.vrInput = QLineEdit(self)

        vthetLabl = QLabel("<i>V<sub>&theta;<\sub><\i>", self)
        self.vthetInput = QLineEdit(self)

        nLabl = QLabel("<i>n<\i>", self)
        self.nInput = QLineEdit(self)

        dtLabl = QLabel("<i>dt<\i>", self)
        self.dtInput = QLineEdit(self)

        self.calcButton = QPushButton('Calculate', self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.dtInput)
        vbox.addWidget(self.calcButton)

        fbox1 = QFormLayout()
        fbox1.addRow(r0Labl, self.r0Input)
        fbox1.addRow(mLabl, self.mInput)
        fbox1.addRow(vthetLabl, self.vthetInput)

        fbox2 = QFormLayout()
        fbox2.addRow(kLabl, self.kInput)
        fbox2.addRow(thetaLabl, self.thetaInput)
        fbox2.addRow(nLabl, self.nInput)

        fbox3 = QFormLayout()
        fbox3.addRow(l0labl, self.l0Input)
        fbox3.addRow(vrLabl, self.vrInput)
        fbox3.addRow(dtLabl, vbox)

        hbox = QHBoxLayout()
        hbox.addLayout(fbox1)
        hbox.addLayout(fbox2)
        hbox.addLayout(fbox3)

        self.calcButton.clicked.connect(self.calculate)

        mainVbox = QVBoxLayout()
        mainVbox.addLayout(hbox)

        self.graphLayout = QHBoxLayout()
        mainVbox.addLayout(self.graphLayout)

        self.setLayout(mainVbox)

    def calculate(self):

        from WidgetsScript import Hamiltonian as Hamil

        m = float(self.mInput.text())
        k = float(self.kInput.text())
        l0 = float(self.l0Input.text())
        r0 = float(self.r0Input.text())
        theta0 = float(self.thetaInput.text())
        vr = float(self.vrInput.text())
        vtheta = float(self.vthetInput.text())
        n = int(self.nInput.text())
        dt = float(self.dtInput.text())

        self.table, self.index = Hamil(m, k, l0, r0, theta0, vr, vtheta, n, dt)

        self.graph()

    def graph(self):

        from PlotGraph import Plot_Graph
        from GraphPlot import GraphPlot

        values = [self.table[self.index[0]], self.table[self.index[3]]]
        names = [self.index[0], self.index[3]]

        graph = GraphPlot(values, names)
        Graphic = Plot_Graph()
        Graphic.set_Hamil_Graph(graph)

        self.graphLayout.addWidget(Graphic)


#########################################
#           Terminal Window             #
#########################################
#
#   This class create the object with the interface
#       required to make a new table or insert a nex column 
#       as a CSV file.
#
##############################################################################

class Terminal_for_table(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.edit = QTextEdit()


        self.edit.canPaste()
        self.edit.append('>>>')

        self.pColButton = QPushButton('Run', self)
        self.pColButton.setShortcut('Ctrl+E')
        self.pColButton.clicked.connect(self.python)

        self.nwTblButton = QPushButton('Clear', self)
        self.nwTblButton.clicked.connect(self.clear)

        hbox.addWidget(self.pColButton)
        hbox.addWidget(self.nwTblButton)

        vbox.addWidget(self.edit)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def python(self):

        text = self.edit.toPlainText().split('>>>')[-1]

        if "..." in text:
        	self.withStatement(text)

        elif ":" in text[-1]:
        	self.edit.append("..."+"\t")

        else:
        	self.normalConsole(text)


    def withStatement(self, text):

    	text = text.split("...")

    	if "\t" not in text[-1]:
    		text = "".join(text)

    		try:
    			exec(text)
    		except (SyntaxError, NameError, TypeError):
    			self.edit.append("Error")

    		self.edit.append(">>>")

    	else:

    		self.edit.append("..."+"\t")

    def normalConsole(self, text):

    	from math import *

        try:

            result = eval(text)

            self.edit.append(str(result) + '\n'+'>>>')

        except (SyntaxError, NameError, TypeError):
            self.edit.append("Error"+"\n"+">>>")

    def clear(self):

        self.edit.clear()
        self.edit.append('>>>')


#########################################
#            Formula Entry              #
#########################################
#
#   This class create the object with the interface
#       required to request the equation necessary to use the
#       Operation class from Calculator
#
##################################################################

class FormulaEntry(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        Formula = QGroupBox()
        Formula.setTitle("Formula Entry")

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.lineEdit = QLineEdit(self)
        self.runButton = QPushButton("Run", self)

        vbox.addWidget(self.lineEdit)
        hbox.addWidget(self.runButton)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        Formula.setLayout(vbox)

        Main = QHBoxLayout()
        Main.addWidget(Formula)

        self.setLayout(Main)


#########################################
#              Graph Axes               #
#########################################
#
#   This class create the object with the interface
#       required to request which columns want to represent
#
##################################################################

class GraphAxes(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        graphics = QGroupBox()
        graphics.setTitle("Graphics")

        axesXLabl = QLabel("<h1>X</h1>", self)

        axesYLabl = QLabel("<h1>Y</h1>", self)

        self.axesXCombo = QComboBox(self)
        self.axesYCombo = QComboBox(self)

        fbox = QFormLayout()
        fbox.addRow(axesXLabl, self.axesXCombo)
        fbox.addRow(axesYLabl, self.axesYCombo)

        hbox = QHBoxLayout()
        self.result = QLabel('', self)
        hbox.addWidget(self.result)

        self.VMainBox = QVBoxLayout()
        self.VMainBox.addLayout(fbox)
        self.VMainBox.addLayout(hbox)

        graphics.setLayout(self.VMainBox)

        self.checkObject()

        Main = QHBoxLayout()
        Main.addWidget(graphics)

        self.setLayout(Main)

    def checkObject(self):
        from PyQt5.QtWidgets import QCheckBox

        self.check = QCheckBox('Replot', self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.check)
        hbox.addStretch(1)

        self.VMainBox.addLayout(hbox)

    def setNames(self, index):

        self.axesXCombo.clear()
        for name in index.values():
            self.axesXCombo.addItem(name)

        self.axesYCombo.clear()
        for name in index.values():
            self.axesYCombo.addItem(name)


#########################################
#              Html View                #
#########################################
#
#   This class create the window to show the README file
#
##########################################################

from PyQt5.QtWidgets import QMainWindow

class HtmlReadme(QMainWindow):

    def __init__(self, parent=None):

        super(HtmlReadme, self).__init__(parent)

        from PyQt5.QtWebKitWidgets import QWebView
        from PyQt5.QtCore import QUrl

        web = QWebView()
        web.load(QUrl("file:///home/jaimedgp/J_Graphics_P/README.html"))

        self.setCentralWidget(web)
