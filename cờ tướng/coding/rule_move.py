selected_pos = None
from frontend import blue_team

from dataclasses import dataclass
@dataclass
class Move:
    row: int
    col: int
    selected_piece: str
    selected_pos: tuple
    board: list
    def __post_init__(self):
        if self.selected_piece in blue_team:
            self.board = [a[::-1] for a in self.board[::-1]]
            self.row = 9 - self.row
            self.col = 8 - self.col
            self.selected_pos = (9 - self.selected_pos[0], 8 - self.selected_pos[1])
    def pawn(self):#"卒", "兵"
        if self.selected_piece in [ "卒", "兵"]:
            if self.row <= 4:
                if self.row ==  self.selected_pos[0] + 1 and self.col ==  self.selected_pos[1]:
                    return True
            else:
                if self.row ==  self.selected_pos[0] + 1 and self.col ==  self.selected_pos[1]:
                    return True
                elif abs(self.col -  self.selected_pos[1]) <= 1 and (self.row ==  self.selected_pos[0]) :
                    return True
        else:       
            return False
    
    def gun(self):
        if self.selected_piece in ["砲", "炮"]:
            if self.row == self.selected_pos[0] or self.col ==  self.selected_pos[1]:  
                if self.row == self.selected_pos[0]:
                    if self.col > self.selected_pos[1]:
                        count = 0
                        for a in range (self.selected_pos[1]+1, self.col+1):
                            if self.board[self.row][a] is not None:
                                if self.board[self.row][self.col] is None:
                                    return False
                                if (a == self.col) and count == 1:
                                    return [True, 'eat']
                                count += 1
                        if self.board[self.row][self.col] is None:
                            return [True, 'move']
                    elif self.col < self.selected_pos[1]:
                        count = 0
                        for a in range(self.selected_pos[1]-1, self.col-1, -1):
                            if self.board[self.row][a] is not None:
                                if self.board[self.row][self.col] is None:
                                    return False
                                if (a == self.col) and count == 1:
                                    return [True, 'eat']
                                count += 1
                        if self.board[self.row][self.col] is None:
                            return [True, 'move']
                elif self.col == self.selected_pos[1]:
                    if self.row > self.selected_pos[0]:
                        count = 0
                        for a in range (self.selected_pos[0]+1, self.row+1):
                            if self.board[a][self.col] is not None:
                                if self.board[self.row][self.col] is None:
                                    return False
                                if (a == self.row) and count == 1:                     
                                    return [True, 'eat']
                                count += 1
                        if self.board[self.row][self.col] is None:                     
                            return [True, 'move']           
                    elif self.row < self.selected_pos[0]:
                        count = 0
                        for a in range(self.selected_pos[0]-1, self.row-1, -1):
                            if self.board[a][self.col] is not None:
                                if self.board[self.row][self.col] is None:
                                    return False
                                if (a == self.row) and count == 1:                     
                                    return [True, 'eat']
                                count += 1
                        if self.board[self.row][self.col] is None:                     
                            return [True, 'move']
    def horse(self):
        if self.selected_piece in ["馬", "傌"]:
            if (abs(self.col - self.selected_pos[1]) == 2 and abs(self.row - self.selected_pos[0]) == 1) or (abs(self.row - self.selected_pos[0]) == 2 and abs(self.col - self.selected_pos[1]) == 1):
                if self.col - self.selected_pos[1] == 2:
                    if self.board[self.selected_pos[0]][self.selected_pos[1]+1] is not None:
                        return False
                if self.col - self.selected_pos[1] == -2:
                    if self.board[self.selected_pos[0]][self.selected_pos[1]-1] is not None:
                        return False
                if self.row - self.selected_pos[0] == 2:
                    if self.board[self.selected_pos[0]+1][self.selected_pos[1]] is not None:
                        return False
                if self.row - self.selected_pos[0] == -2:
                    if self.board[self.selected_pos[0]-1][self.selected_pos[1]] is not None:
                        return False
                return True
                    
    def elephant(self):
        if self.selected_piece in ["相", "象"]:
            if abs(self.col - self.selected_pos[1]) == 2 and abs(self.row - self.selected_pos[0]) == 2 and self.row <= 4:
                if self.col - self.selected_pos[1] == 2 and self.row - self. selected_pos[0] == 2 :
                    if self.board[self.selected_pos[0]+1][self.selected_pos[1]+1] is None:
                        return True
                if self.col - self.selected_pos[1] == 2 and self.row - self.selected_pos[0] == -2 :
                    if self.board[self.selected_pos[0]-1][self.selected_pos[1]+1] is None:
                        return True    
                if self.col - self.selected_pos[1] == -2 and self.row - self.selected_pos[0] == 2:
                    if self.board[self.selected_pos[0]+1][self.selected_pos[1]-1] is None:
                        return True
                if self.col - self.selected_pos[1] == -2 and self.row - self.selected_pos[0] == -2:
                    if self.board[self.selected_pos[0]-1][self.selected_pos[1]-1] is None:
                        return True  
                else:
                    return False      
            else:
                return False
    def body_guard(self):
        if self.selected_piece in ["士", "仕"]:
            if (abs(self.row - self.selected_pos[0]) == 1) and (abs(self.col - self.selected_pos[1]) == 1) and (2 < self.col < 6) and (self.row <= 2):
                return True
            else:
                return False 
    def king(self):
        if self.selected_piece in ["将", "帥"]:
            if (2 < self.col < 6) and (self.row < 3):
                if (abs(self.row - self.selected_pos[0]) == 1) and (self.col == self.selected_pos[1]):
                    return True
                elif (abs(self.col - self.selected_pos[1]) == 1) and (self.row == self.selected_pos[0]):
                    return True 
        else:
            return False                     
    def car(self):
        if self.selected_piece in ["車", "俥"]:
            if self.selected_pos[0] == self.row or self.selected_pos[1] == self.col:
                if self.selected_pos[0] == self.row:
                    if self.selected_pos[1] < self.col:
                        for a in range(self.selected_pos[1]+1, self.col):
                            if self.board[self.row][a] is not None:
                                return False
                        return True
                    elif self.selected_pos[1] > self.col:
                        for a in range(self.selected_pos[1]-1, self.col, -1):
                            if self.board[self.row][a] is not None:
                                return False
                        return True
                elif self.selected_pos[1] == self.col:
                    if self.selected_pos[0] < self.row:
                        for a in range(self.selected_pos[0]+1, self.row):
                            if self.board[a][self.col] is not None:
                                return False
                        return True
                    elif self.selected_pos[0] > self.row:
                        for a in range(self.selected_pos[0]-1, self.row, -1):
                            if self.board[a][self.col] is not None:
                                return False
                        return True

