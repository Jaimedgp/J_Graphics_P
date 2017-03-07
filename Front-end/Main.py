#########################################
#    JDG (Just a Graphics' Printer)	    #
#########################################
#
#	This program has been develop by Jaime Diez Gonzalez-Pardo in Python in
#   	order to facilitate operations in performing laboratory practice
#
#	This class allows to make all the mathematical operations
#
#	Required: 
#
#	Return: 
#
##############################################################################

from PyQt5.QtWidgets import QApplication, QHBoxLayout
from MainWindow import Main_Window_GUI
from MainLayout import MainLayout
import sys

app = QApplication(sys.argv)

mainWindow = Main_Window_GUI()

mainLayout = MainLayout()

mainLayout.showDataLyout()
mainLayout.widgetToolLyout()

mainWindow.addLayout(mainLayout)
mainWindow.show()

sys.exit(app.exec_())