import server
import random
class rps(server.inSock):
    def start(self):
        print('started at %s' % self.ipaddr)
        users = [0 for i in range(self.count)]
    def conv(self,kw):
        data = kw['data']
        chos = ['rock','paper','scissors']
        stro = random.choice(chos)
        return stro
serv = rps('127.0.0.1',5000)
serv.echoServ()
