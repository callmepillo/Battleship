from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Main(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 447)

        #Grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 401, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.cellLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.cellLayout.setContentsMargins(0, 0, 0, 0)
        self.cellLayout.setObjectName("cellLayout")

        #Guess Layout
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 491, 401, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.guessLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.guessLayout.setContentsMargins(0, 0, 0, 0)
        self.guessLayout.setObjectName("guessLayout")

        #Player One Name Label
        self.player_one_name = QtWidgets.QLabel(Form)
        self.player_one_name.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.player_one_name.setFont(font)
        self.player_one_name.setAutoFillBackground(False)
        self.player_one_name.setFrameShape(QtWidgets.QFrame.Panel)
        self.player_one_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_one_name.setAlignment(QtCore.Qt.AlignCenter)
        self.player_one_name.setObjectName("player_one_name")

        # Player Two Name Label
        self.player_two_name = QtWidgets.QLabel(Form)
        self.player_two_name.setGeometry(QtCore.QRect(120, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.player_two_name.setFont(font)
        self.player_two_name.setAutoFillBackground(False)
        self.player_two_name.setFrameShape(QtWidgets.QFrame.Panel)
        self.player_two_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_two_name.setAlignment(QtCore.Qt.AlignCenter)
        self.player_two_name.setObjectName("player_two_name")

        # Current Score Label
        self.current_score = QtWidgets.QLabel(Form)
        self.current_score.setGeometry(QtCore.QRect(330, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.current_score.setFont(font)
        self.current_score.setAutoFillBackground(False)
        self.current_score.setFrameShape(QtWidgets.QFrame.Panel)
        self.current_score.setFrameShadow(QtWidgets.QFrame.Raised)
        self.current_score.setAlignment(QtCore.Qt.AlignCenter)
        self.current_score.setObjectName("current_score")

        # Player Two No. Ships Label
        self.player_two_ships = QtWidgets.QLabel(Form)
        self.player_two_ships.setGeometry(QtCore.QRect(120, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.player_two_ships.setFont(font)
        self.player_two_ships.setAutoFillBackground(False)
        self.player_two_ships.setFrameShape(QtWidgets.QFrame.Panel)
        self.player_two_ships.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_two_ships.setAlignment(QtCore.Qt.AlignCenter)
        self.player_two_ships.setObjectName("player_two_ships")

        # Player One No. Ships Label
        self.player_one_ships = QtWidgets.QLabel(Form)
        self.player_one_ships.setGeometry(QtCore.QRect(10, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.player_one_ships.setFont(font)
        self.player_one_ships.setAutoFillBackground(False)
        self.player_one_ships.setFrameShape(QtWidgets.QFrame.Panel)
        self.player_one_ships.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_one_ships.setAlignment(QtCore.Qt.AlignCenter)
        self.player_one_ships.setObjectName("player_one_ships")

        # New Game Button
        self.end_turn_btn = QtWidgets.QPushButton(Form)
        self.end_turn_btn.setGeometry(QtCore.QRect(240, 50, 81, 31))
        self.end_turn_btn.setObjectName("end_turn_btn")

        # Exit Game Button
        self.exit_game_btn = QtWidgets.QPushButton(Form)
        self.exit_game_btn.setGeometry(QtCore.QRect(330, 50, 81, 31))
        self.exit_game_btn.setObjectName("exit_game_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.player_one_name.setText(_translate("Form", "PLAYER_1"))
        self.player_two_name.setText(_translate("Form", "PLAYER_2"))
        self.current_score.setText(_translate("Form", "SCORE"))
        self.player_two_ships.setText(_translate("Form", "PLAYER_2_SHIPS"))
        self.player_one_ships.setText(_translate("Form", "PLAYER_1_SHIPS"))
        self.end_turn_btn.setText(_translate("Form", "New Game"))
        self.exit_game_btn.setText(_translate("Form", "Exit Game"))

# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#
#         width = 400
#         height = 550
#         self.setFixedSize(width, height)
#
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
# if __name__=="__main__":
#     app = QtWidgets.QApplication([])
#     application = MyWindow()
#     application.show()
#     sys.exit(app.exec())