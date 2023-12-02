from PyQt5 import QtCore, QtGui, QtWidgets
from choose import Ui_secondWindow


class Ui_MainWindow(object):

    # Open the Game Window
    def open_win(self):
        self.game_win = QtWidgets.QMainWindow()
        self.game_ui = Ui_secondWindow()
        self.game_ui.setupUi(self.game_win)
        self.game_win.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 703)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(803, 703))
        MainWindow.setMaximumSize(QtCore.QSize(803, 703))
        font = QtGui.QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 61))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 70, 811, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\img/w2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.play = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_win())
        self.play.setGeometry(QtCore.QRect(240, 590, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(26)
        self.play.setFont(font)
        self.play.setObjectName("play")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors v1.0"))
        MainWindow.setWindowIcon(QtGui.QIcon('img\logo.png'))
        self.label.setText(_translate("MainWindow", "Rock Paper Scissors "))
        self.play.setText(_translate("MainWindow", "Play"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
