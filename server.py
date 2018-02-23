import socket
from threading import Thread as thread
import time
class inSock:
    def __init__(self,*args):
        if len(args) == 0:
            intf = ('localhost',5000)
        if len(args) == 1:
            intf = ('localhost',args[0])
        if len(args) == 2:
            intf = tuple(args)
        if len(args) == 3:
            intf = tuple(args[:2])
            self.numol = args[2]
        else:
            self.numol = 10
        self.count = self.numol
        self.intf = intf
        self.ipaddr = intf[0]
        self.port = intf[1]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(intf)
        self.s.listen(self.numol)
        self.start()
    def start(self):
        pass
    def conv(self,kw):
        return kw['data']
    def echo(self,con):
        #time.sleep(random.randrange(1000)/500)
        conn, addr = self.s.accept()
        while 1:
            try:
                data = conn.recv(1024)
            except ConnectionResetError:
                break
            if data == b'':
                break
            else:
                pass
                #print(str(self.intf[1])+' : %s'% data.decode())
            ret = data.decode('utf8')
            ret = self.conv({'data':ret,'user id':con})
            conn.send(ret.encode('utf8'))
    def echoServ(self):
        dead = [thread(target=self.echo,args=(i,)) for i in range(self.numol)]
        lastdead = [0 for i in range(len(dead))]
        for pl,i in enumerate(dead):
            i.start()
            print('live',pl)
        while 1:
            for pl,i in enumerate(dead):
                if not i.is_alive() and lastdead[pl]:
                    print('dead',pl)
                    dead[pl] = thread(target=self.echo,args=(pl,))
                    dead[pl].start()
                    print('live',pl)
                    lastdead[pl] = False
                    time.sleep(1)
                else:
                    lastdead[pl] = True
    def kill(self):
        self.s.close()
class outSock:
    def __init__(self,*args):
        if len(args) == 0:
            intf = ('localhost',5000)
        if len(args) == 1:
            intf = ('localhost',args[0])
        if len(args) == 2:
            intf = tuple(args)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(intf)
        self.last = None
    def pinger(self):
        las = 0
        while True:
            self.sendStr(str(time.time()-las-1))
            self.recvStr()
            las = time.time()
            time.sleep(1)
    def recvLoop(self):
        while True:
            try:
                print(self.recvStr())
            except:
                pass
                exit()
    def loop(self):
        while True:
            try:
                self.sendStr(input(': '))
                time.sleep(1)
            except KeyboardInterrupt:
                print()
                self.s.close()
                exit()
            except:
                raise
    def send(self,data):
        self.last = data
        self.s.sendall(data)
    def recv(self):
        data = s.recv(1024)
        return data
    def sendStr(self,data):
        self.send(data.encode('utf8'))
    def recvStr(self):
        return self.s.recv(1024).decode('utf8')
    def kill(self):
        self.s.close()
web_ip = socket.gethostname()
print(web_ip)
