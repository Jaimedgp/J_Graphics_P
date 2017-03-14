
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QGroupBox, QComboBox, QTextEdit

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

class CalculateError(QWidget):

	def __init__(self):
	
		super(QWidget, self).__init__()
	
		lbl1 = QLabel("<i>Simbolos<\i>", self)
		self.textbox1 = QLineEdit(self)

		lbl4 = QLabel("<i>Valores<\i>", self)
		self.textbox4 = QLineEdit(self)

		lbl7 = QLabel("<i>Errores<\i>", self)
		self.textbox7 = QLineEdit(self)

		lbl8 = QLabel("<i>f = <\i>", self)
		self.textbox8 = QLineEdit(self)

		hbox = QHBoxLayout()

		button4 = QPushButton('Calculate', self)
		# connect button to function on_click
		button4.clicked.connect(self.CalculateErrors)

		hbox.addWidget(button4)
		hbox.addStretch(1)
		vbox = QVBoxLayout()
		vbox.addWidget(self.textbox8)
		vbox.addLayout(hbox)

		fbox = QFormLayout()
		fbox.addRow(lbl1, self.textbox1)
		fbox.addRow(lbl4, self.textbox4)
		fbox.addRow(lbl7, self.textbox7)
		fbox.addRow(lbl8, vbox)

		self.setLayout(fbox)


	def CalculateErrors(self):

		from WidgetsScrypt import ErrorsCalculator

		symbol = self.textbox1.text()
		values = eval(self.textbox4.text())
		errors = eval(self.textbox7.text())
		function = str(self.textbox8.text())
		
		valorError = ErrorsCalculator(symbol, values, errors, function)


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

class ErrorBars(QWidget):

	def __init__(self, index):

		super(QWidget, self).__init__()

		self.index = index

		self.VBox = QVBoxLayout()
		self.set_Error_By_Column()
		self.set_Error_By_Fixed()
		self.set_Error_By_Percent()

		hBox = QHBoxLayout()

		self.MainCombo = QComboBox(self)
		self.MainCombo.addItem("None")
		self.MainCombo.addItem("% of value")
		self.MainCombo.addItem("Fixed value")
		self.MainCombo.addItem("Data column")
		hBox.addWidget(self.MainCombo)

		VMainBox = QVBoxLayout()
		hBox.addLayout(self.VBox)
		VMainBox.addLayout(hBox)

		self.button = QPushButton('Plot', self)
		VMainBox.addWidget(self.button)

		self.setLayout(VMainBox)

	def set_Error_By_Column(self):

		column = QGroupBox()
		column.setTitle('Data Column')

		vbox = QVBoxLayout()

		self.combo = QComboBox(self)
		for name in self.index.values():
			self.combo.addItem(name)

		vbox.addWidget(self.combo)
		column.setLayout(vbox)
		self.VBox.addWidget(column)

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
		self.percenteg = QLineEdit()
		vbox.addWidget(self.percenteg)
		Percent.setLayout(vbox)

		self.VBox.addWidget(Percent)


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

class Hamiltonian(QWidget):

	def __init__(self):

		super(QWidget, self).__init__()

		lbl1 = QLabel("<i>r<sub>0<\sub><\i>", self)
		self.textbox1 = QLineEdit(self)

		lbl2 = QLabel("<i>k<\i>", self)
		self.textbox2 = QLineEdit(self)

		lbl3 = QLabel("<i>l<sub>0<\sub><\i>", self)
		self.textbox3 = QLineEdit(self)

		lbl4 = QLabel("Masa/g", self)
		self.textbox4 = QLineEdit(self)

		lbl5 = QLabel(u'\u03B8', self)
		self.textbox5 = QLineEdit(self)

		lbl6 = QLabel("<i>V<sub>r<\sub><\i>", self)
		self.textbox6 = QLineEdit(self)

		lbl7 = QLabel("<i>V<sub>&theta;<\sub><\i>", self)
		self.textbox7 = QLineEdit(self)

		lbl8 = QLabel("<i>n<\i>", self)
		self.textbox8 = QLineEdit(self)

		lbl9 = QLabel("<i>dt<\i>", self)
		self.textbox9 = QLineEdit(self)

		self.button4 = QPushButton('Calculate', self)

		vbox = QVBoxLayout()
		vbox.addWidget(self.textbox9)
		vbox.addWidget(self.button4)

		fbox1 = QFormLayout()
		fbox1.addRow(lbl1, self.textbox1)
		fbox1.addRow(lbl4, self.textbox4)
		fbox1.addRow(lbl7, self.textbox7)

		fbox2 = QFormLayout()
		fbox2.addRow(lbl2, self.textbox2)
		fbox2.addRow(lbl5, self.textbox5)
		fbox2.addRow(lbl8, self.textbox8)

		fbox3 = QFormLayout()
		fbox3.addRow(lbl3, self.textbox3)
		fbox3.addRow(lbl6, self.textbox6)
		fbox3.addRow(lbl9, vbox)

		hbox = QHBoxLayout()
		hbox.addLayout(fbox1)
		hbox.addLayout(fbox2)
		hbox.addLayout(fbox3)

		self.button4.clicked.connect(self.calculate)

		self.setLayout(hbox)

	def calculate(self):

		m = float(self.textbox4.text())
		k = float(self.textbox2.text())
		l0 = float(self.textbox3.text())
		r0 = float(self.textbox1.text())
		theta0 = float(self.textbox5.text())
		vr = float(self.textbox6.text())
		vtheta = float(self.textbox7.text())
		n = int(self.textbox8.text())
		dt = float(self.textbox9.text())

		self.Path = Hamiltonian(m, k, l0, r0, theta0, vr, vtheta, n, dt)



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

class Terminal_for_table(QWidget):

	def __init__(self):

		super(QWidget, self).__init__()

		vbox = QVBoxLayout()
		hbox = QHBoxLayout()

		self.edit = QTextEdit()
		self.button1 = QPushButton('Add Columns', self)
		#self.button1.clicked.connect(self.doAddColumns)
		self.button2 = QPushButton('New Table', self)
		#self.button2.clicked.connect(self.doChangeColumns)

		hbox.addWidget(self.button1)
		hbox.addWidget(self.button2)

		vbox.addWidget(self.edit)
		vbox.addLayout(hbox)

		self.setLayout(vbox)