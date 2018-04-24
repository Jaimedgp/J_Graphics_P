#########################################
#              Main Window              #
#########################################
#
#   this class is my class and in my class I write what I want
#
#   Required: 
#
#   Return: 
#
################################################################################

from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication, QFileDialog,
                                                   QInputDialog, QMessageBox)
from PyQt5.QtGui import QIcon

from MainLayout import MainLayout
from MainTabses import TabMain

from WidgetsScript import derivative
from OpenScript import Open_file_CSV, Open_file_TXT
from SaveScript import saveCSV, saveTXT, saveLaTex

import os
import sys

class Main_Window_GUI(QMainWindow):

    def __init__(self, pathIcon, pathInicProyect):

        super(QMainWindow, self).__init__()

        self.pathInicProyect = pathInicProyect
        self.TAB = []
        self.setGeometry(0, 0, 2000, 1100)
        self.setWindowTitle("Just a Graphics Printer")
        self.setWindowIcon(
            QIcon(pathIcon))

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
        graphMenu = menubar.addMenu('&Graph')
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

        self.TAB.append(mainLayout2)

        tabLayout.addTabs(mainLayout2)

    def closeProject(self):

        if not self.TAB[tabLayout.currentIndex()].dataSaved:

            reply = QMessageBox.information(self, ' ',
                                            "Save changes before closing?",
                                                       ( QMessageBox.Save |
                                                       QMessageBox.Cancel |
                                                      QMessageBox.Discard),
                                                          QMessageBox.Save)

            if reply == QMessageBox.Save:

                self.save()

            elif reply == QMessageBox.Discard:

                del self.TAB[tabLayout.currentIndex()]

                tabLayout.deleteTabs(tabLayout.currentIndex())

        else:

            del self.TAB[tabLayout.currentIndex()]

            tabLayout.deleteTabs(tabLayout.currentIndex())

    def openFile(self):

        tab = self.TAB[tabLayout.currentIndex()]
        fileName, ok = QFileDialog.getOpenFileName(self, 'Open file',
                                       self.pathInicProyect, 'Text File (*.csv *.txt)')

        if ok:

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

            self.TAB[tabLayout.currentIndex()].dataTable.reDoTable()

    def save(self):
        if self.TAB[tabLayout.currentIndex()].path != '/':

            if ".csv" in self.TAB[tabLayout.currentIndex()].path:
                saveCSV(self.TAB[tabLayout.currentIndex()].dataTable.table,
                        self.TAB[tabLayout.currentIndex()].dataTable.index,
                                             self.TAB[tabLayout.currentIndex()].path)

            elif ".txt" in self.TAB[tabLayout.currentIndex()].path:
                saveTXT(self.TAB[tabLayout.currentIndex()].dataTable.table,
                        self.TAB[tabLayout.currentIndex()].dataTable.index,
                                             self.TAB[tabLayout.currentIndex()].path)
        else:
            self.saveAs()

        self.TAB[tabLayout.currentIndex()].dataSaved = True

    def saveAs(self):

        fname, ok = QFileDialog.getSaveFileName(self, 'Open file',
                                  self.TAB[tabLayout.currentIndex()].path,
                                                   "Calc files (*.csv *.txt)")

        if ok:

            self.TAB[tabLayout.currentIndex()].path = str(fname)

            if ".csv" in self.TAB[tabLayout.currentIndex()].path:
                saveCSV(self.TAB[tabLayout.currentIndex()].dataTable.table,
                          self.TAB[tabLayout.currentIndex()].dataTable.index,
                                          self.TAB[tabLayout.currentIndex()].path)

                name = self.TAB[tabLayout.currentIndex()].path.split(".csv")[0]

            elif ".txt" in self.TAB[tabLayout.currentIndex()].path:
                saveTXT(self.TAB[tabLayout.currentIndex()].dataTable.table,
                          self.TAB[tabLayout.currentIndex()].dataTable.index,
                                             self.TAB[tabLayout.currentIndex()].path)

                name = self.TAB[tabLayout.currentIndex()].path.split(".txt")[0]

            self.TAB[tabLayout.currentIndex()].dataSaved = True

            tabLayout.tabMain.setTabText(tabLayout.currentIndex(),
                                                                name.split("/")[-1])

    def saveIntoTex(self):

        text, ok = QInputDialog.getText(self, 'Export LaTex', 
                              '    Columns <h6>e.j."1,2" for columns C1'+ 
                                      ' and C2<\h6> or "all" for all table:')
        if ok:
            #CHANGE
            fname, ok = (QFileDialog.getSaveFileName(self, 'Open file',
                                      self.TAB[tabLayout.currentIndex()].path,
                                                       "LaTex files (*.tex)"))
        if text == 'all':
            saveLaTex(self.TAB[tabLayout.currentIndex()].dataTable.table,
                      self.TAB[tabLayout.currentIndex()].dataTable.index,
                      self.TAB[tabLayout.currentIndex()].dataTable.index.keys(),
                                                                   fname)
        else:

            saveLaTex(self.TAB[tabLayout.currentIndex()].dataTable.table,
                      self.TAB[tabLayout.currentIndex()].dataTable.index,
                                                       eval(text), fname)

    def differential(self):

        text, ok = QInputDialog.getText(self, 'Derivative',
                              '    Columns <h6>e.j."1,2" for columns C1'+
                                                           ' and C2<\h6> :')
        if ok:
            derivative(self.TAB[tabLayout.currentIndex()].dataTable.table,
                      self.TAB[tabLayout.currentIndex()].dataTable.index,
                                                                 eval(text))

        self.TAB[tabLayout.currentIndex()].dataTable.reDoTable()
        self.TAB[tabLayout.currentIndex()].dataSaved = True

    def saveFigure(self):

        self.TAB[tabLayout.currentIndex()].saveGraph()

    def graphdot(self):

        self.TAB[tabLayout.currentIndex()].plotGraph('o')

    def graphline(self):

        self.TAB[tabLayout.currentIndex()].plotGraph('')

    def linearGraph(self):

        self.TAB[tabLayout.currentIndex()].plotRegressionGraph('lin')

    def logarithmicGraph(self):

        self.TAB[tabLayout.currentIndex()].plotRegressionGraph('log')

    def exponentialGraph(self):

        self.TAB[tabLayout.currentIndex()].plotRegressionGraph('exp')

    def polynomialGraph(self):

        self.TAB[tabLayout.currentIndex()].plotRegressionGraph('poly')

    def pepepeGraph(self):

        self.TAB[tabLayout.currentIndex()].plotRegressionGraph('pepe')

    def CurveFitGraph(self):

        self.TAB[tabLayout.currentIndex()].plotRegressionGraph('general')

    def closeEvent(self, event):

        boolean = True

        for tab in self.TAB:
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

                for tab in self.TAB:
                    if not tab.dataSaved:

                        fname, ok = (QFileDialog.getSaveFileName(self,'Open file',
                                self.pathInicProyect, "Calc files (*.csv *.txt)"))
                        saveCSV(tab.dataTable.table, tab.dataTable.index,
                                fname)

                event.accept()

            elif reply == QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()

    def addLayout(self, layout):

        self.setCentralWidget(layout)


if __name__ == '__main__':

    home = os.path.expanduser("~")

    os.chdir(home)

    for root, dirs, files in os.walk(os.path.abspath("J_Graphics_P"), topdown=True):
        for name in files:
            if name.endswith(("Photos", "JGP(icon).png")):
                pathIcon = os.path.join(root, "JGP(icon).png")

    app = QApplication(sys.argv)

    tabLayout = TabMain()

    mainLayout = MainLayout()

    tabLayout.addTabs(mainLayout)

    ex = Main_Window_GUI(pathIcon, home)
    ex.addLayout(tabLayout)
    ex.TAB = [mainLayout]
    ex.show()
    sys.exit(app.exec_())
