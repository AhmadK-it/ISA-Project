from state import State 
import copy as cp
from board import Cell 

class Game:
    def __init__(self):
        self.init= open('test_board_1.txt')
        self.test1= open('test_board_2.txt')
        self.test2= open('test_board_3.txt')
        self.board = self.initBoard(self.test2)
        self.initState = State(self.board)
    
    
    def initBoard(self, file , n = 4 , m=7):
        board = [[Cell(row, col) for col in range(m)] for row in range(n)]

        data = list()
        for x in file:
            data.append(x.split(','))

        tmp = list()
        final = dict()
        i=0
        for ls in data:
            for x in ls:
                if x != '\n':
                    st1,st2 = x.split('-')
                    tmp.append([int(st1),st2])
            final[i]=cp.copy(tmp)
            tmp.clear()
            i+=1

        for key in final.keys():
            for ls in final[key]:
                board[key][ls[0]].struct.type=ls[1]
                if ls[1] == 'P0' or ls[1] == 'P1':
                    board[key][ls[0]].struct.mail = 1
        
        file.close()
        return board




