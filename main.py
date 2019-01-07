from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSizePolicy

class Application:
    def __init__(self):
        self.qt_app = QApplication([])
        self.qt_app.setApplicationName("DevWindow")
        self.window = QWidget()

        self.main_layout = QHBoxLayout()

        self.createSidepanel()
        self.createCenterPlayerListUI()

        #self.main_layout.addWidget(QPushButton("Hello"))
        #self.main_layout.addWidget(QPushButton("World"))

        self.window.setLayout(self.main_layout)
        self.window.setWindowTitle("DevWindow")

        self.window.show()
        self.qt_app.exec_()

    def createSidepanel(self):
        self.sidePanelWidget = QWidget()
        self.sidePanelLayout = QVBoxLayout()

        self.sidePanelLayout.addWidget(QLabel("Side Panel"))

        self.sidePanelWidget.setLayout(self.sidePanelLayout)
        self.main_layout.addWidget(self.sidePanelWidget)

    def createCenterPlayerListUI(self):
        self.centerVerticalWidget = QWidget()
        self.centerVerticalLayout = QVBoxLayout()

        self.centerVerticalLayout.addWidget(QLabel("Tool and Search bar"))
        self.centerVerticalLayout.addWidget(QLabel("Search Results"))

        def createToolAndSearchBar(self):
            pass

        def createResultsList(self):
            pass

        def createBottomPlayerControls(self):
            self.bottomPlayerWidget = QWidget()
            self.bottomPlayerLayout = QHBoxLayout()

            self.bottomPlayerLayout.addWidget(QPushButton("Prev"))
            self.bottomPlayerLayout.addWidget(QPushButton("Play"))
            self.bottomPlayerLayout.addWidget(QPushButton("Next"))

            sizePolicy = QSizePolicy()
            sizePolicy.setVerticalStretch(1)
            self.bottomPlayerWidget.setSizePolicy(sizePolicy)

            self.bottomPlayerWidget.setLayout(self.bottomPlayerLayout)
            self.centerVerticalLayout.addWidget(self.bottomPlayerWidget)

        # NOTE(Dustin): Order here matters
        createToolAndSearchBar(self)
        createResultsList(self)
        createBottomPlayerControls(self)

        self.centerVerticalWidget.setLayout(self.centerVerticalLayout)
        self.main_layout.addWidget(self.centerVerticalWidget)

    def run(self):
        pass

if __name__=="__main__":
    Application().run()
