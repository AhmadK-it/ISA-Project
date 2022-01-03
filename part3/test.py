from game import Game

g = Game()
# g.initBoard(g.init)
g.initState.printBoard()
tmp = g.initState.nextState(g.initState)
tt = list()
print(tmp)

for t in tmp :
    print('1','\n')
    t.printBoard()
    print('carried: ',t.carried, '\twaited: ', t.waited)
    a = t.nextState(t)

for x in a :
    print('2','\n')
    x.printBoard()
    
    print('carried: ',x.carried, '\twaited: ', x.waited)
    # for y in x.resM:
    #     print(y.mail,y.type)
    r = x.nextState(x)
    tt.append(r)
alpha = list()
# print(tt)
for ls in tt:
    for x in ls :
        print('3','\n')
        print('carried: ',x.carried, '\twaited: ', x.waited)
    # for y in x.resM:
        # for y in x.resM:
        #     print(y.mail,y.type)
        x.printBoard()
        print('hi',x.board[1][3].struct.mail)
        s = x.nextState(x)
        alpha.append(s)

# print(alpha)