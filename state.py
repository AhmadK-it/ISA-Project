import copy as cp 

class State:
    def __init__(self, playBoard):
        self.board = cp.deepcopy(playBoard)
    
    def printBoard(self):
        size = len(self.board)
        for key in range(1,size,5):
            print('--|---|---|---|---')
            print(self.board[key],'|',
                self.board[key+1],'|',
                self.board[key+2],'|',
                self.board[key+3],'|',
                self.board[key+4])
            print('--|---|---|---|---')
        print('\n')