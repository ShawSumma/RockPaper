import server
import random
class rps(server.inSock):
    def start(self):
        print('started at %s' % self.ipaddr)
        users = [0 for i in range(self.count)]
    def conv(self,kw):
        data = kw['data']
        if data[0] == '!':
            k = data[1:].split(' ')[0]
            data = data[len(k)+1:]
            if k == 'echo':
                k = data[1:].split(' ')[0]
                data = data[len(k)+1:]
                return data
            if k == 'whoami':
                return str(kw['user id'])
            if k == 'dm':
                k = data[1:].split(' ')[0]
                data = data[len(k)+1:]
                if k == 'list':
                    pass
                self.broadcast[int(k)].append({kw['user id']:data})
        return ''
serv = rps('127.0.0.1',5000)
serv.echoServ()
