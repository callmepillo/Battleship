import os
from sys import flags

import sysv_ipc
from sysv_ipc import IPC_CREAT, ExistentialError, BusyError


# 1 -> String/Normal Message
# 2 -> State

class State:
    def __init__(self, src):
        self.matrix = list()
        for row in src.split(';'):
            if row.strip():
                a = list()
                for elem in row.split(' '):
                    if elem.isdigit():
                        a.append(int(elem.strip()))
                self.matrix.append(a)

    def stateFromString(self, src):
        self.matrix = list()
        for row in src.split(';'):
            if row.strip():
                a = list()
                for elem in row.split(' '):
                    if elem.isdigit():
                        a.append(int(elem.strip()))
                self.matrix.append(a)

    def toString(self):
        res = " "
        for row in self.matrix:
            for elem in row:
                res = res + str(elem) + " "
            res = res + "; "
        return res

class MessageQueueHandler:
    def __init__(self, username):
        self.key = -1
        self.username = username
        self.queue = None
        self.opponent_connected = False
        self.send_channel = -1
        self.receive_channel = -1
        self.host = False

    def connect(self, msg_key):
        self.key = msg_key
        try:
            self.queue = sysv_ipc.MessageQueue(self.key)
            self.queue.send(str(os.getpid()), True, 1)
            self.wait_for_partner()
        except ExistentialError:
            self.queue = sysv_ipc.MessageQueue(self.key, sysv_ipc.IPC_CREX)
            self.clear()
            self.host = True
            self.wait_for_partner()
            #self.queue.send(str(0), False, 3)

        print("Message queue initialized. " + self.username + " connected to key: " + str(self.key) + "\nMy PID is: " + str(os.getpid()))
        #(count,_) = self.queue.receive(False, 3)
        #count = count + 1
        #self.queue.send(str(count), False, 3)

    def clear(self):
        while True:
            try:
                self.queue.receive(block=False)  # Non-blocking receive
            except sysv_ipc.BusyError:
                break

    def disconnect(self):
        if self.queue is None:
            return
        try:
            self.queue.remove()
            print("Message queue was deleted.")
        except ExistentialError:
            return

    def watcher(self):
        if self.queue is None:
            print("Message queue dosent exist.")
            self.queue = None  # Mark as deleted
            self.opponent_connected = False
            return False
        try:
            _ = self.queue.current_messages
            try:
                self.receive_messages()
            except BusyError:
                pass

        except sysv_ipc.ExistentialError:
            print("Message queue was deleted.")
            self.queue = None  # Mark as deleted
            self.opponent_connected = False
            return False
        return True

    def queue_is_full(self):
        count = 0
        try:
            for item in self.queue.receive(False, 3):
                if type(item) == bytes:
                    count = int(item)
        except BusyError:
            return False
        if count > 1:
            return True
        else:
            return False

    def wait_for_partner(self):
        rejected = True
        for item in self.queue.receive(True):
            if type(item) == bytes and int(item.decode()) != os.getpid():
                if not self.opponent_connected:
                    rejected = False
                    self.send_channel = int(item.decode())
                    self.receive_channel = os.getpid()
                    self.opponent_connected = True
                    if self.host:
                        self.queue.send(str(os.getpid()), True, 1)
                    print(str(self.send_channel) + " connected.")
        if rejected:
            #self.disconnect()
            self.queue = None
            self.opponent_connected = False
            self.send_channel = 1
            self.host = False
            self.key = -1

    def send_username(self):
        if self.opponent_connected:
            self.queue.send(self.username, False, self.send_channel)


    def send_message(self, message, msg_type):
        self.queue.send(message, False, self.send_channel + msg_type)

    def get_key(self):
        return self.queue.key

    def receive_username(self):
        for item in self.queue.receive(False, self.receive_channel):
            if type(item) == bytes:
                return item.decode()

    def receive_messages(self):
        for item in self.queue.receive(False, self.receive_channel + 1):
            if type(item) == bytes:
                print("received: {}".format(item.decode()))

    def receive_state(self):
        for item in self.queue.receive(True, self.receive_channel + 2):
            if type(item) == bytes:
                state = State(item.decode())
                print("received state: {}".format(state.toString()))
                return state



