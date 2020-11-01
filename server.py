import threading
import socket
import os
import sys



class Server(threading.Thread):
    def __init__(self, sc, socket, server):
        super().__init__()
        self.sc = sc
        self.socket = socket
        self.server = server
        
        def run(self):
    while True:
        ipt = input()
        if ipt == '/quit': Bye
