from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout

class TabMain(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        layout = QVBoxLayout()

        self.tabMain = QTabWidget()
        layout.addWidget(self.tabMain)

        self.setLayout(layout)

    def currentIndex(self):

        return self.tabMain.currentIndex()

    def deleteTabs(self, int):

        self.tabMain.removeTab(int)

    def addTabs(self, layout):

        self.tabMain.addTab(layout, "Data %s" %(self.tabMain.count()+1))
