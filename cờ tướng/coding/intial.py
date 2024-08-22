from abletomove import expect_move
import copy, math, sys
import numpy as np
from frontend import pygame

from frontend import padding_x, padding_y, circle_diameter, circle_radius, red_team, blue_team
from protectking import protect_king
from sound import SoundManager, gay_can
from checkwin import check_win
from frontend import draw_board, draw_pieces



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
    # turn = 0
    sound = False
    sound_2 = False
    step = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and step == 0:
                x, y = event.pos
                col = (x - padding_x) // circle_diameter
                row = (y - padding_y) // circle_diameter
                if 0 <= col < 9 and 0 <= row < 10:
                    piece_center_x = padding_x + col * circle_diameter + circle_radius
                    piece_center_y = padding_y + row * circle_diameter + circle_radius

                    distance = math.sqrt((x - piece_center_x) ** 2 + (y - piece_center_y) ** 2)
                    if distance <= circle_radius:  # Kiểm tra xem điểm chuột có nằm trong hình tròn quân cờ không
                        selected_piece = board[row][col]
                        selected_pos = (row, col)
                        if selected_piece is not None:
                            box = expect_move(selected_piece, selected_pos, board)[0]
                            step = 1
                                        
            elif event.type == pygame.MOUSEBUTTONDOWN and step == 1:
                step = 0
                if selected_piece is not None:
                    x, y = event.pos
                    col = (x - padding_x) // circle_diameter
                    row = (y - padding_y) // circle_diameter
                    if 0 <= col < 9 and 0 <= row < 10 and (row, col) != selected_pos:# (king, id_king, board):["将", "帥"]
                        if selected_piece in red_team :
                            if (row, col) in box :#and protect_king("将", formatted_position, board):# and turn == 0 :
                                flat = False
                                if board[row][col] is not None:
                                    history = board[row][col]
                                    flat = True
                                board[selected_pos[0]][selected_pos[1]] = None
                                board[row][col] = selected_piece
                                board_array = np.array(board)
                                position = np.where(board_array == "将")
                                formatted_position = (position[0][0], position[1][0])
                                if protect_king("将", formatted_position, board) == False:
                                        board[selected_pos[0]][selected_pos[1]] = selected_piece
                                        # click = True
                                        if flat:
                                            board[row][col] = history
                                        else:
                                            board[row][col] = None
                                if flat:
                                    sound_manager.danh_kiem()
                                if check_win('blue', board) == (False, 'blue'):
                                    print('red win')
                                sound_manager.move()
                                if gay_can('red', board):
                                    sound_manager.play_nervous()
                                    sound = True
                                else:
                                    sound = False
                                
                                # turn = 1 - turn
                        elif selected_piece in blue_team:
                            if (row, col) in box:# and protect_king("帥", formatted_position_blue, board):# and turn == 1 :
                                flat = False

                                if board[row][col] is not None:
                                    flat = True
                                board[selected_pos[0]][selected_pos[1]] = None
                                board[row][col] = selected_piece 
                                board_array = np.array(board)
                                position_blue = np.where(board_array == "帥")
                                formatted_position_blue = (position_blue[0][0], position_blue[1][0])
                                
                                if protect_king("帥", formatted_position_blue, board) == False:
                                        board[selected_pos[0]][selected_pos[1]] = selected_piece
                                        if flat:
                                            board[row][col] = history
                                        else:
                                            board[row][col] = None
                                            
                                if flat:
                                    sound_manager.danh_kiem()
                                if check_win('red', board) == (False, 'red'):
                                    print('blue win')
                                sound_manager.move()
                                # turn = 1 - turn
                                
                                
                            if gay_can('blue', board):
                                sound_manager.play_nervous()
                                sound_2 = True
                            else:
                                sound_2 = False
                                # print(gay_can('blue', board))
                if sound == False and sound_2 == False:
                    sound_manager.stop_nervous()                
                                
                selected_piece = None
                selected_pos = None
                                        
        draw_board()
        draw_pieces(board= board)
        pygame.display.flip()

game_loop()
# check win
# sound 
# image beauty ful