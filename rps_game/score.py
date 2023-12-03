from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog, computer, user):
        Dialog.setObjectName("Dialog")
        Dialog.resize(272, 109)
        Dialog.setMinimumSize(QtCore.QSize(272, 109))
        Dialog.setMaximumSize(QtCore.QSize(272, 109))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.compute_score = QtWidgets.QLCDNumber(Dialog)
        self.compute_score.setGeometry(QtCore.QRect(20, 40, 91, 61))
        self.compute_score.setObjectName("compute_score")
        # Display Computer Score
        self.compute_score.display(computer)

        self.user_score = QtWidgets.QLCDNumber(Dialog)
        self.user_score.setGeometry(QtCore.QRect(160, 40, 91, 61))
        self.user_score.setObjectName("user_score")
        # Display User Score
        self.user_score.display(user)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Score Board"))
        Dialog.setWindowIcon(QtGui.QIcon(r'rps_game\img\logo.png'))
        self.label.setText(_translate("Dialog", "Computer"))
        self.label_2.setText(_translate("Dialog", "You"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
