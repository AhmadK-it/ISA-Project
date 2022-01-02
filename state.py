import copy as cp 

class State:
    def __init__(self, playBoard , row=4 , col=7):
        self.board = cp.deepcopy(playBoard)
        self.n = row
        self.m = col
    
    def printBoard(self):
        types = [[str(self.board[row][col].struct.type) for col in range(self.m)] for row in range(self.n)]
        for t in types:
            print("---------------------------------------------------")
            print('  |   '.join(t))
            print("---------------------------------------------------")
            
    
    def move(self,row,col,listStates,state):
        current = cp.deepcopy(state)
        n = current.getRows()
        m = current.getCols()
        type = current.board[row][col].struct.type
        if type == '. ' or type == 'D0' or type == 'D1'or type == 'P0' or type == 'P1':
            if row-1>=0:
                if current.board[row-1][col].struct.type == 'T ':
                    tmp = current.vMove('D',type,row,col,current)
                    listStates.append(tmp)
            if row+1<n:
                if current.board[row+1][col].struct.type == 'T ':
                    tmp = current.vMove('U',type,row,col,current)
                    listStates.append(tmp)
            if col-1>=0:
                if current.board[row][col-1].struct.type == 'T ':
                    tmp = current.hMove('R',type,row,col,current)
                    listStates.append(tmp)
            if col+1<m:
                if current.board[row][col+1].struct.type == 'T ':
                    tmp = current.hMove('L',type,row,col,current)
                    listStates.append(tmp)
        
    def vMove(self,Dir,type,row,col,state):
        if Dir == 'U':
            state.board[row][col].struct.type = 'T '
            state.board[row+1][col].struct.type = '. '
            if type != '. ':
                print(True)
        else:
            state.board[row][col].struct.type = 'T '
            state.board[row-1][col].struct.type = '. '
            if type != '. ':
                    print(True)
        return state
    def hMove(self,Dir,type,row,col,state):
        if Dir == 'R':
            state.board[row][col].struct.type = 'T '
            state.board[row][col-1].struct.type = '. '
            if type != '. ':
                    print(True)
        else:
            state.board[row][col].struct.type = 'T '
            state.board[row][col+1].struct.type = '. '
            if type != '. ':
                    print(True)
        return state
    
    def nextState(self,state):
        current = cp.deepcopy(state)
        nextStattes = list()

        for row in range(self.n):
            for col in range(self.m):
                self.move(row,col,nextStattes,current)
        return nextStattes
    
    def getBoard(self):
        return self.board
    
    def getRows(self):
        return self.n
    def getCols(self):
        return self.m