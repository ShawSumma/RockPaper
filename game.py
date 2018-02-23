import server
import shutil
import time
import random
class xSock(server.outSock):
    def printOut(self):
        while True:
            print('out ->', self.recvStr())
            time.sleep(0.1)
    def loopFn(self):
        global count
        count += 1
        server.thread(target =self.printOut).start()
        while True:
            r = self.sendStr(input('in -> '))
            time.sleep(0.1)
user = xSock('127.0.0.1',5000)
count = 0
while True:
    t = server.thread(target=user.loopFn)
    t.start()
    time.sleep(0)
    break
