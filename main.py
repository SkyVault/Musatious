from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSlider
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSizePolicy, QStyle
from PyQt5.QtCore import Qt


def getHorizontalSizePolicy(n=0):
    sizePolicy = QSizePolicy()
    sizePolicy.setHorizontalPolicy(n)
    return sizePolicy


def getVerticalSizePolicy(n=0):
    sizePolicy = QSizePolicy()
    sizePolicy.setVerticalPolicy(n)
    return sizePolicy


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

        def createToolAndSearchBar(self):
            self.toolBarWidget = QWidget()
            self.toolBarLayout = QVBoxLayout()

            self.toolBarLayout.addWidget(QLabel("Tool and Search bar"))

            sizePolicy = QSizePolicy()
            sizePolicy.setVerticalStretch(2)
            self.toolBarWidget.setSizePolicy(sizePolicy)

            self.toolBarWidget.setLayout(self.toolBarLayout)
            self.centerVerticalLayout.addWidget(self.toolBarWidget)

        def createResultsList(self):
            self.resultsListWidget = QWidget()
            self.resultsListLayout = QVBoxLayout()

            self.resultsListLayout.addWidget(QLabel("Results List"))

            sizePolicy = QSizePolicy()
            sizePolicy.setVerticalStretch(8)
            self.resultsListWidget.setSizePolicy(sizePolicy)

            self.resultsListWidget.setLayout(self.resultsListLayout)
            self.centerVerticalLayout.addWidget(self.resultsListWidget)

        def createBottomPlayerControls(self):
            self.bottomPlayerWidget = QWidget()
            self.bottomPlayerLayout = QHBoxLayout()

            self.playbackSlider = QSlider(Qt.Horizontal)

            self.playToggle = QPushButton()
            self.playToggle.setIcon(self.bottomPlayerWidget.style().standardIcon(QStyle.SP_MediaPlay))

            self.songPrev = QPushButton()
            self.songPrev.setIcon(self.bottomPlayerWidget.style().standardIcon(QStyle.SP_MediaSkipBackward))

            self.songNext = QPushButton()
            self.songNext.setIcon(self.bottomPlayerWidget.style().standardIcon(QStyle.SP_MediaSkipForward))

            self.bottomPlayerLayout.addWidget(self.playbackSlider)

            self.bottomPlayerLayout.addWidget(self.songPrev)
            self.bottomPlayerLayout.addWidget(self.playToggle)
            self.bottomPlayerLayout.addWidget(self.songNext)

            sizePolicy = QSizePolicy()
            sizePolicy.setVerticalStretch(0)
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
