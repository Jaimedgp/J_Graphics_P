#########################################
#              Main Window              #
#########################################
#
#   this class is my class and in my class I write what I want
# ejemplo para inigo
#   This class allows to make all the mathematical operations
#
#   Required: 
#
#   Return: 
#
################################################################################

from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication, QFileDialog, 
                                                   QInputDialog, QMessageBox)
from PyQt5.QtGui import QIcon
import sys

from MainLayout import MainLayout
from MainTabses import TabMain

from WidgetsScript import derivative
from OpenScript import Open_file_CSV, Open_file_TXT
from SaveScript import saveCSV, saveTXT, saveLaTex

class Main_Window_GUI(QMainWindow):

    def __init__(self):

        super(QMainWindow, self).__init__()

        self.setGeometry(0, 0, 2000, 1100)
        self.setWindowTitle("Just a Graphics Printer")
        self.setWindowIcon(
            QIcon("../J_Graphics_P/Photos/JGP(icon).png"))

        self.fileMenuBar()
        self.graphMenuBar()
        self.toolsMenuBar()

    def fileMenuBar(self):

        openProject = QAction('Open Project', self)
        openProject.setShortcut('Ctrl+T')
        openProject.triggered.connect(self.openAProject)

        deleteProject = QAction('Delete Project', self)
        deleteProject.setShortcut('Ctrl+W')
        deleteProject.triggered.connect(self.closeProject)

        openAction = QAction('Open file', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a table from a file')
        openAction.triggered.connect(self.openFile)

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save table')
        saveAction.triggered.connect(self.save)

        saveAs = QAction('Save as', self)
        saveAs.setShortcut('Ctrl+Shift+S')
        saveAs.setStatusTip('Save table')
        saveAs.triggered.connect(self.saveAs)

        savepng = QAction('Save Figure', self)
        savepng.setStatusTip('Save Figure')
        savepng.triggered.connect(self.saveFigure)

        saveTex = QAction('Export to LaTeX', self)
        saveTex.setStatusTip('Export table to LaTex code')
        saveTex.triggered.connect(self.saveIntoTex)

        exitAction = QAction('Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openProject)
        fileMenu.addAction(deleteProject)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAs)
        fileMenu.addAction(savepng)
        fileMenu.addAction(saveTex)
        fileMenu.addAction(exitAction)

    def graphMenuBar(self):

        GraphDots = QAction('Dots', self)
        GraphDots.setShortcut('Ctrl+G')
        GraphDots.triggered.connect(self.graphdot)

        GraphLine = QAction('Line', self)
        GraphLine.triggered.connect(self.graphline)

        linearGraph = QAction('Linear', self)
        linearGraph.setStatusTip('y = a*x + b')
        linearGraph.triggered.connect(self.linearGraph)

        CurveFitGraph = QAction('Curve Fit', self)
        CurveFitGraph.triggered.connect(self.CurveFitGraph)

        logGraph = QAction('Logarithmic', self)
        logGraph.setStatusTip('a*log(x) + b')
        logGraph.triggered.connect(self.logarithmicGraph)

        expGraph = QAction('Exponential', self)
        expGraph.setStatusTip('b * e^(a*x)')
        expGraph.triggered.connect(self.exponentialGraph)

        polyGraph = QAction('Polynomial', self)
        polyGraph.triggered.connect(self.polynomialGraph)

        pepepeGraph = QAction('Pepe', self)
        pepepeGraph.setStatusTip('a*x^m')
        pepepeGraph.triggered.connect(self.pepepeGraph)

        self.statusBar()

        menubar = self.menuBar()
        graphMenu = menubar.addMenu('&Curve Fit')
        simpleGraph = graphMenu.addMenu('Graphic')
        simpleGraph.addAction(GraphDots)
        simpleGraph.addAction(GraphLine)
        graphMenu.addSeparator()
        graphMenu.addAction(linearGraph)
        graphMenu.addAction(CurveFitGraph)
        graphMenu.addAction(logGraph)
        graphMenu.addAction(expGraph)
        graphMenu.addAction(polyGraph)
        graphMenu.addAction(pepepeGraph)

    def toolsMenuBar(self):

        diffCalculator = QAction('Derivative', self)
        diffCalculator.setStatusTip('Calculate the derivative between two columns')
        diffCalculator.triggered.connect(self.differential)

        helpView = QAction('Help', self)
        helpView.setStatusTip('Open the README help')
        helpView.triggered.connect(self.html)

        self.statusBar()

        menubar = self.menuBar()
        toolsMenu = menubar.addMenu('&Tools')
        toolsMenu.addAction(diffCalculator)
        toolsMenu.addAction(helpView)

    def html(self):

        from ToolsWidgets import HtmlReadme

        self.window = HtmlReadme(self)
        self.window.show()

    def openAProject(self):
        mainLayout2 = MainLayout()

        TAB.append(mainLayout2)

        tabLayout.addTabs(mainLayout2)

    def closeProject(self):

        if not TAB[tabLayout.currentIndex()].dataSaved:

            reply = QMessageBox.information(self, ' ', 
                                            "Save changes before closing?", 
                                                       ( QMessageBox.Save | 
                                                       QMessageBox.Cancel | 
                                                      QMessageBox.Discard), 
                                                          QMessageBox.Save)

            if reply == QMessageBox.Save:

                self.save()

            elif reply == QMessageBox.Discard:

                del TAB[tabLayout.currentIndex()]

                tabLayout.deleteTabs(tabLayout.currentIndex())

        else:

            del TAB[tabLayout.currentIndex()]

            tabLayout.deleteTabs(tabLayout.currentIndex())

    def openFile(self):
        
        tab = TAB[tabLayout.currentIndex()]
        fileName, ok = QFileDialog.getOpenFileName(self, 'Open file',
                                       '/home/jaime', 'Text File (*.csv *.txt)')

        if '/home/jaime' in fileName:

            if ".csv" in fileName:
                table, index = Open_file_CSV(fileName)
                name = fileName.split(".csv")[0]
            elif ".txt" in fileName:
                table, index = Open_file_TXT(fileName)
                name = fileName.split(".txt")[0]

            tab.path = fileName
            tab.dataTable.table = table
            tab.dataTable.index = index
            tab.ErrBar.set_new_Columns_names(tab.dataTable.index)
            tab.GrphAxes.setNames(tab.dataTable.index)

            tabLayout.tabMain.setTabText(tabLayout.currentIndex(),
                                                            name.split("/")[-1])

            TAB[tabLayout.currentIndex()].dataTable.reDoTable()

    def save(self):
        if TAB[tabLayout.currentIndex()].path != '/':

            if ".csv" in TAB[tabLayout.currentIndex()].path:
                saveCSV(TAB[tabLayout.currentIndex()].dataTable.table, 
                        TAB[tabLayout.currentIndex()].dataTable.index,
                                             TAB[tabLayout.currentIndex()].path)    
        
            elif ".txt" in TAB[tabLayout.currentIndex()].path:
                saveTXT(TAB[tabLayout.currentIndex()].dataTable.table, 
                        TAB[tabLayout.currentIndex()].dataTable.index,
                                             TAB[tabLayout.currentIndex()].path)
        else:
        	self.saveAs()

        TAB[tabLayout.currentIndex()].dataSaved = True

    def saveAs(self):

        fname, ok = QFileDialog.getSaveFileName(self, 'Open file',
                                  TAB[tabLayout.currentIndex()].path, 
                                                   "Calc files (*.csv *.txt)")
        
        if ok:

	        TAB[tabLayout.currentIndex()].path = str(fname)

	        if ".csv" in TAB[tabLayout.currentIndex()].path:
	            saveCSV(TAB[tabLayout.currentIndex()].dataTable.table, 
	                      TAB[tabLayout.currentIndex()].dataTable.index, 
	                                      TAB[tabLayout.currentIndex()].path)

	            name = TAB[tabLayout.currentIndex()].path.split(".csv")[0]

	        elif ".txt" in TAB[tabLayout.currentIndex()].path:
	            saveTXT(TAB[tabLayout.currentIndex()].dataTable.table, 
	                      TAB[tabLayout.currentIndex()].dataTable.index, 
	                                      TAB[tabLayout.currentIndex()].path)
	            
	            name = TAB[tabLayout.currentIndex()].path.split(".txt")[0]

	        TAB[tabLayout.currentIndex()].dataSaved = True

	        tabLayout.tabMain.setTabText(tabLayout.currentIndex(),
	                                                        name.split("/")[-1])

    def saveIntoTex(self):

        text, ok = QInputDialog.getText(self, 'Export LaTex', 
                              '    Columns <h6>e.j."1,2" for columns C1'+ 
                                      ' and C2<\h6> or "all" for all table:')
        if ok:
            fname = str(QFileDialog.getSaveFileName(self, 'Open file',
                                      TAB[tabLayout.currentIndex()].path, "LaTex files (*.tex)"))
            fname = fname.split(',')[0]
            fname = fname.split('(u')
            fname = fname[1].split("'")

        if text == 'all':
            saveLaTex(TAB[tabLayout.currentIndex()].dataTable.table,
                      TAB[tabLayout.currentIndex()].dataTable.index,
                      TAB[tabLayout.currentIndex()].dataTable.index.keys(),
                                                                   fname[1])
        else:

            saveLaTex(TAB[tabLayout.currentIndex()].dataTable.table,
                      TAB[tabLayout.currentIndex()].dataTable.index,
                                                       eval(text), fname[1])
    
    def differential(self):

        text, ok = QInputDialog.getText(self, 'Derivative',
                              '    Columns <h6>e.j."1,2" for columns C1'+
                                                           ' and C2<\h6> :')
        if ok:
            derivative(TAB[tabLayout.currentIndex()].dataTable.table,
                      TAB[tabLayout.currentIndex()].dataTable.index,
                                                                 eval(text))

        TAB[tabLayout.currentIndex()].dataTable.reDoTable()
        TAB[tabLayout.currentIndex()].dataSaved = True

    def saveFigure(self):

        TAB[tabLayout.currentIndex()].saveGraph()

    def graphdot(self):

        TAB[tabLayout.currentIndex()].plotGraph('ro')

    def graphline(self):

        TAB[tabLayout.currentIndex()].plotGraph('b')

    def linearGraph(self):

        TAB[tabLayout.currentIndex()].plotLinearGraph()

    def logarithmicGraph(self):

        TAB[tabLayout.currentIndex()].plotLogGraph()

    def exponentialGraph(self):

        TAB[tabLayout.currentIndex()].plotExpGraph()

    def polynomialGraph(self):

        TAB[tabLayout.currentIndex()].plotPolyGraph()

    def pepepeGraph(self):

        TAB[tabLayout.currentIndex()].plotPepeGraph()

    def CurveFitGraph(self):

        TAB[tabLayout.currentIndex()].plotCurveFitgraph()    

    def closeEvent(self, event):

        boolean = True

        for tab in TAB:
            if not tab.dataSaved:
                boolean = False

        if boolean:

            event.accept()

        else:

            reply = QMessageBox.information(self, ' ', "Save changes before"+
                                            "closing", (QMessageBox.Save | 
                                                      QMessageBox.Cancel |
                                                      QMessageBox.Discard),
                                                             QMessageBox.Save)

            if reply == QMessageBox.Save:

                for tab in TAB:
                    if not tab.dataSaved:

                        fname = str(QFileDialog.getSaveFileName(self,'Open file',
                                     '/home/jaime/', "Calc files (*.csv *.txt)"))
                        fname = fname.split(',')[0]
                        fname = fname.split('(u')
                        fname = fname[1].split("'")

                        saveCSV(tab.dataTable.table, tab.dataTable.index,
                                                                        fname[1])

                event.accept()

            elif reply == QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()

    def addLayout(self, layout):

        self.setCentralWidget(layout)


#########################################
#              Main Window              #
#########################################
#
#   FALTA EL COMANDO SELF.SHOW()
#
#   This class allows to make all the mathematical operations
#
#   Required: 
#
#   Return: 
#
##############################################################################

if __name__ == '__main__':

    app = QApplication(sys.argv)

    tabLayout = TabMain()

    mainLayout = MainLayout()

    TAB = [mainLayout]

    tabLayout.addTabs(mainLayout)

    ex = Main_Window_GUI()
    ex.addLayout(tabLayout)
    ex.show()
    sys.exit(app.exec_())
