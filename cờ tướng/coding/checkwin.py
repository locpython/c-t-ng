from abletomove import expect_move
import copy
import numpy as np
from protectking import protect_king

red_team =  ["車" , "馬", "相", "士", "将", "砲", "卒"]
blue_team = ["俥", "傌", "象", "仕", "帥", "炮", "兵"]
def check_win(team, board):
    flat = False
    winner = team
    if team == 'red': # thủ
        for a in range(10):
            for b in range(9):
                if board[a][b] is not None:
                    if board[a][b] in red_team:
                        selected_piece = board[a][b]
                        selected_pos = (a, b)
                        box = expect_move(selected_piece, selected_pos, board)[0]
                        for c in box:
                            if protect_king("将", board, c, selected_pos, selected_piece) == True:#protect_king(king, board_ảo, plan, selected_pos, selected_piece)
                                    flat = True
                                    winner = None
                                    break
                if flat:
                    break
    elif team == 'blue': # tấn công
        for a in range(10):
            for b in range(9):
                if board[a][b] is not None:
                    if board[a][b] in blue_team:
                        board_ảo = copy.deepcopy(board)
                        selected_piece = board[a][b]
                        selected_pos = (a, b)
                        box = expect_move(selected_piece, selected_pos, board)[0]
                        # print(selected_piece, box)"帥"
                        for c in box:
                            if protect_king("帥", board, c, selected_pos, selected_piece) == True:#protect_king(king, board_ảo, plan, selected_pos, selected_piece)
                                    flat = True
                                    winner = None
                                    break
                if flat:
                    break                
    return flat, winner