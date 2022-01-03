import copy as cp 

class State:
    def __init__(self, playBoard , row=4 , col=7):
        self.board = cp.deepcopy(playBoard)
        self.n = row
        self.m = col
        self.parent = None
        self.resM = list()
        self.delevM = list()
        self.cost = 1
        self.carried = 0
        self.waited = 0
        
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
            struct = cp.copy(state.board[row][col].struct)
            state.checkPoints(type, struct, state.resM, state.delevM)
            state.board[row][col].struct.type = 'T '
            state.board[row][col].struct.mail = state.board[row+1][col].struct.mail
            state.board[row+1][col].struct.type = '. '
            state.board[row+1][col].struct.mail = 0
        else:
            struct = cp.copy(state.board[row][col].struct)
            state.checkPoints(type, struct, state.resM, state.delevM)
            state.board[row][col].struct.type = 'T '
            state.board[row][col].struct.mail = state.board[row-1][col].struct.mail
            state.board[row-1][col].struct.type = '. '
            state.board[row-1][col].struct.mail = 0

        for point in state.resM:
            if state.board[point.row][point.col].struct.type != 'T ':
                state.board[point.row][point.col].struct.type = point.type
                state.board[point.row][point.col].struct.mail = point.mail
        for point in state.delevM:
            if state.board[point.row][point.col].struct.type == '. ':
                state.board[point.row][point.col].struct.type = point.type
                state.board[point.row][point.col].struct.mail = point.mail
        return state

    def hMove(self,Dir,type,row,col,state):
        if Dir == 'R':
            struct = cp.copy(state.board[row][col].struct)
            state.checkPoints(type, struct, state.resM, state.delevM)
            state.board[row][col].struct.type = 'T '
            state.board[row][col].struct.mail = state.board[row][col-1].struct.mail
            state.board[row][col-1].struct.type = '. '
            state.board[row][col-1].struct.mail = 0
        else:
            struct = cp.copy(state.board[row][col].struct)
            state.checkPoints(type, struct, state.resM, state.delevM)
            state.board[row][col].struct.type = 'T '
            state.board[row][col].struct.mail = state.board[row][col+1].struct.mail
            state.board[row][col+1].struct.type = '. '
            state.board[row][col+1].struct.mail = 0
        for point in state.resM:
            if state.board[point.row][point.col].struct.type != 'T ':
                state.board[point.row][point.col].struct.type = point.type
                state.board[point.row][point.col].struct.mail = point.mail
        for point in state.delevM:
            if state.board[point.row][point.col].struct.type == '. ':
                state.board[point.row][point.col].struct.type = point.type
                state.board[point.row][point.col].struct.mail = point.mail
        return state
    
    def nextState(self,state):
        current = cp.deepcopy(state)
        nextStattes = list()
        for row in range(self.n):
            for col in range(self.m):
                self.move(row,col,nextStattes,current)
        return nextStattes

    def checkPoints(self , type,struct, listP,listD):
        if type == 'P0' or type == 'P1':
                if struct not in listP:
                    listP.append(struct)
        if type == 'D0' or type == 'D1':
                if struct not in listD:
                    listD.append(struct)
    
    
    #. for setting the Carried mail on the Truck
    def setCarriedMail(self, state,struct, truck):
        if struct.type == 'P0'or struct.type == 'P1':
            state.carried+= struct.mail
            if struct.mail > 0:
                struct.mail-= 1
            truck.mail+= struct.mail
        n = state.getRows()
        m = state.getCols()
        for row in range(n):
            for col in range(m):
                struct = state.board[row][col].struct
                if struct.type == 'D0'or struct.type == 'D1':
                    state.carried-= struct.mail

    #. for seting the waiting mail
    def setWaitedMail(self, state):
        n = state.getRows()
        m = state.getCols()
        count =0 
        for row in range(n):
            for col in range(m):
                struct = state.board[row][col].struct
                if struct.type == 'P0'or struct.type == 'P1':
                    count+= struct.mail
        state.waited = count + state.carried
        for row in range(n):
            for col in range(m):
                struct = state.board[row][col].struct
                if struct.type == 'D0'or struct.type == 'D1':
                    state.carried-= struct.mail

                    
    def setDelevMail(self, state, struct , truck ):
        truck.mail -= 1
        struct.mail += 1
        state.carried -= 1
        state.waited -= 1

    def isGoal(self):
        pass
    def getBoard(self):
        return self.board
    def setParent(self,state):
        self.parent = state
    def getRows(self):
        return self.n
    def getCols(self):
        return self.m
