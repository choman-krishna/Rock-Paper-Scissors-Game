from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):

        super(MyGUI, self).__init__()
        uic.loadUi('rps.ui', self)
        self.show()

        #Basic setup
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setWindowIcon(QIcon("img\logo.png"))

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()
