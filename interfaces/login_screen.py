from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 157)

        # Title Label
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(10, 10, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # Username Input LineEdit
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(50, 80, 113, 25))
        self.username.setObjectName("username")

        # Join Game Button
        self.join_game_btn = QtWidgets.QPushButton(Form)
        self.join_game_btn.setGeometry(QtCore.QRect(50, 110, 111, 25))
        self.join_game_btn.setObjectName("join_game_btn")

        # Exit Game Button
        self.exit_game_btn = QtWidgets.QPushButton(Form)
        self.exit_game_btn.setGeometry(QtCore.QRect(170, 110, 111, 25))
        self.exit_game_btn.setObjectName("exit_game_btn")

        # Message Queue LineEdit
        self.message_queue_key = QtWidgets.QLineEdit(Form)
        self.message_queue_key.setGeometry(QtCore.QRect(170, 80, 113, 25))
        self.message_queue_key.setObjectName("message_queue_key")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "BATTLESHIP"))
        self.join_game_btn.setText(_translate("Form", "Join Game"))
        self.exit_game_btn.setText(_translate("Form", "Exit Game"))
