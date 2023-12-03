from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from score import Ui_Dialog


class Ui_secondWindow(object):

    
    def game_logic(self, user_choice):

        self.user_choice = user_choice
        
        # Generate Random
        self.computer_choice = randint(0,2)

        
        # Game-Logic
        if self.user_choice == self.computer_choice:
            print("Draw")
            self.win_stat = self.result = 0
            
            
        elif self.user_choice + self.computer_choice == 2:
            print("You Loose" if self.computer_choice == 0 else "You Win")  
            self.result = 3
            self.win_stat = 2 if self.computer_choice == 0 else 1
        else:
            print("You Loose" if self.user_choice < self.computer_choice else "You Win")
            self.result = self.computer_choice if self.user_choice < self.computer_choice else self.user_choice
            self.win_stat = 2 if self.user_choice < self.computer_choice else 1
            
        self.close_win(self.result, self.win_stat)

    # Close Win
    def close_win(self, index, win_stat):


        # Message Box
        box_msg = QtWidgets.QMessageBox()
        box_msg.setWindowTitle("Play Again")
        box_msg.setWindowIcon(QtGui.QIcon(r'rps_game\img\logo.png'))

        # Font 
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(20)
        font.setFamily("Georgia")
        box_msg.setFont(font)

        box_msg.setStyleSheet("QLabel { font-size: 15pt; min-height: 100px;}")

        # Image display
        self.index = index
        self.img_list = [r'rps_game\img\draw.jpg', r'rps_game\img\pvr.jpg', r'rps_game\img\svp.jpg', r'rps_game\img\svr.jpg']
        box_msg.setIconPixmap(QtGui.QPixmap(self.img_list[self.index]).scaled(600, 300))        

        # Display Text
        self.win_stat = win_stat
        self.result_list = ['Its Draw', 'You Win', 'You Loose']
        box_msg.setText(self.result_list[self.win_stat])

        # Push Button
        exit_button = box_msg.addButton("Exit",QtWidgets.QMessageBox.RejectRole)
        box_msg.addButton("Play Again",QtWidgets.QMessageBox.NoRole)
        exit_button.clicked.connect(exit)
        box_msg.exec_()

    # Score Board
    def view_score(self, computer_score, user_score):
        self.score_board = QtWidgets.QDialog()
        self.score_ui = Ui_Dialog()
        self.score_ui.setupUi(self.score_board)        

        self.score_board.show()

    def setupUi(self, secondWindow):

        secondWindow.setObjectName("secondWindow")
        secondWindow.resize(620, 481)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(secondWindow.sizePolicy().hasHeightForWidth())
        secondWindow.setSizePolicy(sizePolicy)
        secondWindow.setMinimumSize(QtCore.QSize(620, 481))
        secondWindow.setMaximumSize(QtCore.QSize(620, 481))
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Rock
        self.rock = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.game_logic(0))
        self.rock.setGeometry(QtCore.QRect(20, 20, 271, 161))
        self.rock.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rock.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"rps_game\img\rock_j.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rock.setIcon(icon)
        self.rock.setIconSize(QtCore.QSize(250, 500))
        self.rock.setCheckable(True)
        self.rock.setObjectName("rock")

        # Scissors
        self.scissors = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.game_logic(2))
        self.scissors.setGeometry(QtCore.QRect(180, 220, 281, 171))
        self.scissors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scissors.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"rps_game\img\scissors.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scissors.setIcon(icon1)
        self.scissors.setIconSize(QtCore.QSize(300, 500))
        self.scissors.setObjectName("scissors")

        # Paper
        self.paper = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.game_logic(1))
        self.paper.setGeometry(QtCore.QRect(330, 20, 271, 161))
        self.paper.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paper.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"rps_game\img\paper.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paper.setIcon(icon2)
        self.paper.setIconSize(QtCore.QSize(350, 200))
        self.paper.setObjectName("paper")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 190, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        secondWindow.setCentralWidget(self.centralwidget)
        
        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(secondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        secondWindow.setMenuBar(self.menubar)
        
        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(secondWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuExit.addAction(self.actionQuit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "PLAY"))
        secondWindow.setWindowIcon(QtGui.QIcon(r'rps_game\img\logo.png'))
        self.label.setText(_translate("secondWindow", "Rock"))
        self.label_2.setText(_translate("secondWindow", "Paper"))
        self.label_3.setText(_translate("secondWindow", "Scissors"))
        self.menuExit.setTitle(_translate("secondWindow", "Exit"))
        self.actionQuit.setText(_translate("secondWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
