from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout

class TabMain(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        layout = QVBoxLayout()

        self.tabMain = QTabWidget()
        self.tabMain.setMovable(True)
        layout.addWidget(self.tabMain)

        self.setLayout(layout)

    def currentTab(self):

        return str(self.tabMain.tabText(self.tabMain.currentIndex()))

    def deleteTabs(self, int):

        self.tabMain.removeTab(int)

    def addTabs(self, layout):

        self.tabMain.addTab(layout, "Data %s" %(self.tabMain.count()+1))
