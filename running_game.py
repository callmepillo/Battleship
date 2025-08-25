from PyQt5 import QtWidgets, QtCore

from interfaces.main_interface import Ui_Form_Main
from sender_receiver_systemV import *
from functools import partial

class GameWindow(QtWidgets.QWidget):
    msg_queue = None
    username = None
    state = None
    op_state = None
    def __init__(self, msg_queue, username):
        super(GameWindow, self).__init__()
        self.msg_queue = msg_queue
        self.username = username
        self.state = State(" 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0;")
        self.op_state = None

        width = 422
        height = 507
        self.setFixedSize(width, height)

        self.ui = Ui_Form_Main()
        self.ui.setupUi(self)

        self.ui.end_turn_btn.clicked.connect(self.end_plan)

        self.ui.player_one_ships.setText(str(10))
        self.ui.player_two_ships.setText(str(10))
        self.updateCells()

    def updateCells(self):
        for row_index in range(len(self.state.matrix)):
            for cell_index in range(len(self.state.matrix[0])):
                cell = QtWidgets.QPushButton(self)
                cell.setFixedHeight(75)
                if self.state.matrix[row_index][cell_index]:
                    cell.setStyleSheet('background: rgb(0,0,0)')
                else:
                    cell.setStyleSheet('background: rgb(255,0,0)')
                self.ui.cellLayout.addWidget(cell, row_index, cell_index)
                cell.clicked.connect(partial(self.toggleShip, row_index, cell_index))

    def updateUsernames(self):
        self.msg_queue.send_username()
        self.ui.player_one_name.setText(self.username)
        self.ui.player_two_name.setText(self.msg_queue.receive_username())

    def send_msg(self):
        key = self.msg_queue.get_key()
        self.msg_queue.send_message(self.username + " connected to " + str(key), 1)

    def end_plan(self):
        self.msg_queue.send_message(self.state.toString(), 2)
        # string = self.state.toString()
        # print(string)
        # newState = State(string)
        # print(newState.toString())
        self.receive_state()
        # self.updateCells()
        self.add_guessing_grid()

    def add_guessing_grid(self):

        width = 422
        height = 907
        self.setFixedSize(width, height)

        for row_index in range(len(self.op_state.matrix)):
            for cell_index in range(len(self.op_state.matrix[0])):
                cell = QtWidgets.QPushButton(self)
                cell.setFixedHeight(75)
                # if self.op_state.matrix[row_index][cell_index]:
                #     cell.setStyleSheet('background: rgb(0,0,0)')
                # else:
                #     cell.setStyleSheet('background: rgb(0,0,255)')
                cell.setStyleSheet('background: rgb(0,0,255)')
                self.ui.guessLayout.addWidget(cell, row_index, cell_index)
                cell.clicked.connect(partial(self.guessShip, row_index, cell_index))


    def receive_state(self):
        self.op_state = self.msg_queue.receive_state()

    def toggleShip(self, row, coll):
        if not self.state.matrix[row][coll]:
            btn = self.ui.cellLayout.itemAtPosition(row, coll).widget()
            btn.setStyleSheet('background: rgb(0,0,0)')
            self.state.matrix[row][coll] = 1
        else:
            btn = self.ui.cellLayout.itemAtPosition(row, coll).widget()
            btn.setStyleSheet('background: rgb(255,255,255)')
            self.state.matrix[row][coll] = 0

    def disc(self):
        if self.msg_queue:
            self.msg_queue.disconnect()
            self.msg_queue = None
        #print(self.username)
        self.close()

def runMainGame(msq_queue):
    application = GameWindow(msq_queue, None)
    application.show()
