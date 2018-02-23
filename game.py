import server
import shutil

user = server.outSock('127.0.0.1',5000)

wins = {
    'rock' : 'scissors',
    'paper' : 'rock',
    'scissors' : 'paper',
}
while True:
    try:
        i = input('user : ').lower()
        user.sendStr('ready')
        a = user.recvStr()
        print('ai   : ', a)
        if i[0] == '!':
            if i[1] == 'c':
                for i in range(shutil.get_terminal_size((80, 20))[1]):
                    print()
            continue
        if not i in wins:
            print('options are : %s' % str(list(wins)))
            continue
        if wins[i] == a:
            print('the player wins')
        elif wins[a] == i:
            print('the ai won')
        else:
            print('it was a tie')
        print()
    except KeyboardInterrupt:
        user.kill()
        exit()
