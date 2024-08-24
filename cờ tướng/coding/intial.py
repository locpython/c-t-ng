import copy, sys, math
import numpy as np


from abletomove import expect_move
from frontend import pygame, padding_x, padding_y, circle_diameter, circle_radius, red_team, blue_team, draw_board, draw_pieces
from sound import SoundManager, gay_can
from checkwin import check_win



def rule_move(selected_piece, selected_pos, board_move_1):
    rule = expect_move(selected_piece, selected_pos, board_move_1)
    board_move_2 = copy.deepcopy(board_move_1)
    for a in rule[0]:
        row = a[0]
        col = a[1]
        board_move_2[row][col] = "x"  
    return board_move_2
sound_manager = SoundManager()

board = [
    ["車", "馬", "相", "士", "将", "士", "相", "馬", "車"],
    [None, None, None, None, None, None, None, None, None],
    [None, "砲", None, None, None, None, None, "砲", None],
    ["卒", None, "卒", None, "卒", None, "卒", None, "卒"],
    [None, None, None, None, None, None, None, None, None],
    
    [None, None, None, None, None, None, None, None, None],
    ["兵", None, "兵", None, "兵", None, "兵", None, "兵"],
    [None, "炮", None, None, None, None, None, "炮", None],
    [None, None, None, None, None, None, None, None, None],
    ["俥", "傌", "象", "仕", "帥", "仕", "象", "傌", "俥"]
]
def game_loop():
    global board
    selected_piece = None
    selected_pos = None
    sound = False
    sound_2 = False
    step = 0
    luot = 0
    AI = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            from ModelAI_minimax import comp_move
            if AI == True and luot == 1:
                luot = 1 - luot
                best_move, best_value, best_label, best_position = comp_move(board)
                if best_position is not None  and best_move is not None:
                    board[best_position[0]][best_position[1]] = None
                    board[best_move[0]][best_move[1]] = best_label
                    sound_manager.move()     
                
                
            elif event.type == pygame.MOUSEBUTTONDOWN and step == 0:
                x, y = event.pos
                from distance import hàm_tính_khoảng_cách_con_chuột
                selected_piece, selected_pos, valid, step = hàm_tính_khoảng_cách_con_chuột(x, y, padding_x, padding_y, circle_diameter, circle_radius, board)
                # print(selected_piece, selected_pos, valid, step)

            elif event.type == pygame.MOUSEBUTTONDOWN and step == 1 and selected_piece is not None:
                step = 0
                x, y = event.pos
                col = (x - padding_x) // circle_diameter
                row = (y - padding_y) // circle_diameter                
                
                
                if 0 <= col < 9 and 0 <= row < 10 and (row, col) != selected_pos:# (king, id_king, board):["将", "帥"]          
                    if selected_piece in red_team and AI == False:
                        if (row, col) in valid and luot == 1:
                            luot = 1 - luot
                            if board[row][col] is not None:
                                sound_manager.danh_kiem()  
                            board[selected_pos[0]][selected_pos[1]] = None # chọn
                            board[row][col] = selected_piece    
                            
                            sound_manager.move()                 

                            if check_win('blue', board) == (False, 'blue'):
                                print('red win')
                            if gay_can('red', board):
                                sound_manager.play_nervous()
                                sound = True
                            else:
                                sound = False
                            
                    elif selected_piece in blue_team:
                        if (row, col) in valid and luot == 0:
                            luot = 1 - luot
                            if board[row][col] is not None:
                                sound_manager.danh_kiem() 
                            print(board[selected_pos[0]][selected_pos[1]])    
                            board[selected_pos[0]][selected_pos[1]] = None # chọn
                            board[row][col] = selected_piece
                            
                            sound_manager.move()    
                            
                            if check_win('red', board) == (False, 'red'):
                                print('blue win')
                            
                        if gay_can('blue', board):
                            sound_manager.play_nervous()
                            sound_2 = True
                        else:
                            sound_2 = False
                if sound == False and sound_2 == False:
                    sound_manager.stop_nervous()                
                            
                selected_piece = None
                selected_pos = None
            # print(step)                                
        draw_board()
        draw_pieces(board = board)
        pygame.display.flip()

game_loop()