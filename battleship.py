import sys
from sender_receiver_systemV import *
from login_page import LoginWindow
from running_game import GameWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.msg_queue = None
        self.login_window = LoginWindow()
        self.game_window = GameWindow(None, None)

        self.game_window.hide()
        self.login_window.show()

        self.login_window.ui.join_game_btn.clicked.connect(self.connectGame)
        self.game_window.ui.exit_game_btn.clicked.connect(self.exitSession)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_opponent_connected)

    def connectGame(self):
        self.game_window.msg_queue = MessageQueueHandler(self.login_window.ui.username.text())
        self.game_window.msg_queue.connect(int(self.login_window.ui.message_queue_key.text()))
        ## self.game_window.msg_queue.disconnect()
        if not self.game_window.msg_queue.watcher():
           return
        self.timer.start(1000)  # Check every 1 second
        self.game_window.username = self.login_window.ui.username.text()
        self.game_window.updateUsernames()
        self.login_window.hide()
        self.game_window.show()

    def exitSession(self):
        self.timer.stop()
        self.game_window.disc()
        self.game_window.hide()
        self.login_window.show()

    def check_opponent_connected(self):
        if self.game_window.msg_queue is None:
            print("Message queue dosent exist.")
            self.game_window.msg_queue = None  # Mark as deleted
            self.exitSession()
        if not self.game_window.msg_queue.watcher():
            self.game_window.msg_queue = None  # Mark as deleted
            self.exitSession()

if __name__=="__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    sys.exit(app.exec())