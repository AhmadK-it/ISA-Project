
class Cell:
    def __init__(self , row, col):
        self.row = row
        self.col = col 
        self.struct = Struct(row,col)
        

class Struct:
    def __init__(self, row, col, type='. ', mail=0):
        self.row = row
        self.col = col 
        self.type = type
        self.mail = mail
        
    def setMail(self,mail):
        if mail:
            return 1
        return 0