from state import State 
import random as rand

class Game:
    def __init__(self):
        self.board = self.initBoard()
        self.initState = State(self.board)
    def initBoard(self):
        s = 0
        while True:
            tmp = int(input('Enter size of City (must be divided by 5 ): ')) 
            if tmp % 5 == 0:
                s = tmp +1
                break
            else:
                print('sorry enter valid number as required')
        b = 0
        while True:
            tmp = int(input('Enter number of Buildings: '))
            if tmp <= s-1:
                b = tmp
                break
            else:
                print('sorry')

        board = dict()
        for x in range(1,s,1):
            if b == s-1:
                board[x]='#'
            else:
                board[x]='.'
        
        for x in range(b):
            pos = rand.randint(1, s)
            board[pos] = '#'
        
        return  board
    
    


g = Game()
g.initState.printBoard()
# print(g.board)