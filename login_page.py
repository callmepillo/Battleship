from PyQt5 import QtWidgets
from interfaces.login_screen import Ui_Form_Login
from sender_receiver_systemV import *
from running_game import GameWindow

class LoginWindow(QtWidgets.QWidget):
    msg_queue = None
    def __init__(self):
        super(LoginWindow, self).__init__()

        width = 332
        height = 157
        self.setFixedSize(width, height)

        self.ui = Ui_Form_Login()
        self.ui.setupUi(self)
        self.ui.exit_game_btn.clicked.connect(self.exitGame)
        #self.ui.join_game_btn.clicked.connect(connectGame)

    def exitGame(self):
        self.close()

def showLoginScreen():
    application = LoginWindow()
    application.show()