import pygame
import sys
import numpy as np
import math
import copy
import time

font_path = r"C:\Users\lusan\OneDrive\Desktop\simsun.ttf"
pygame.init()

window_size = (1200, 1040)  
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Cờ Tướng')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (158, 1, 1)  
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

ALL = (175, 103, 55)
quan_co = (222, 186, 140)
ban_co = (211, 137, 79)
mau_vien = (132, 67, 30)

padding_x = 150
padding_y = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

image_width = 800 # Kích thước thực tế của hình ảnh bàn cờ
image_height = 800

# Đường kính và bán kính của hình tròn quân cờ
circle_diameter = 100
circle_radius = circle_diameter // 2

# Define the red and blue team pieces
red_team = ['piece1', 'piece2']  # replace with your actual pieces
blue_team = ['piece3', 'piece4']  # replace with your actual pieces

# Vẽ bảng cờ
def draw_board():
    screen.fill(WHITE)
    #màu bàn cờ : 213 143 86
    # màu viền cờ: 171 100 53
    # màu quân trắng: 229 192 142
    pygame.draw.rect(screen, ALL,(padding_x,
                                            padding_y,
                                            9 * circle_diameter, 10 * circle_diameter))
    pygame.draw.rect(screen, ban_co,(padding_x + 0 * circle_diameter + circle_radius,
                                                        padding_y + 0 * circle_diameter+ circle_radius,
                                                        8 * circle_diameter, 9 * circle_diameter))
    for row in range(9):  # Thay đổi thành 10 hàng
        if row != 4:
            for col in range(8):  # Thay đổi thành 9 cột
                pygame.draw.rect(screen, mau_vien, pygame.Rect(padding_x + col * circle_diameter + circle_radius,
                                                            padding_y + row * circle_diameter+ circle_radius,
                                                            circle_diameter, circle_diameter), 1)
                # print()
    pygame.draw.rect(screen, mau_vien, (padding_x + circle_radius, 
                                       padding_y + circle_radius, 
                                    8 * circle_diameter, 
                                     9 * circle_diameter), 5)     
           
    pygame.draw.rect(screen, mau_vien, (padding_x + circle_radius, 
                                       padding_y + 4 * circle_diameter + circle_radius, 
                                    8 * circle_diameter, 
                                    circle_diameter), 2)                
                
                
                
                
    pygame.draw.line(screen, mau_vien, (padding_x + 3 * circle_diameter + circle_radius, 
                                     padding_y + 7 * circle_diameter + circle_radius), 
                                    (padding_x + 5 * circle_diameter + circle_radius, 
                                     padding_y + 9 * circle_diameter + circle_radius), 3)
    
    pygame.draw.line(screen, mau_vien, (padding_x + 5 * circle_diameter + circle_radius, 
                                     padding_y + 7 * circle_diameter + circle_radius), 
                                    (padding_x + 3 * circle_diameter + circle_radius, 
                                     padding_y + 9 * circle_diameter + circle_radius), 3)
    
    # Cung tướng bên trên
    pygame.draw.line(screen, mau_vien, (padding_x + 3 * circle_diameter + circle_radius, 
                                     padding_y + 0 * circle_diameter + circle_radius), 
                                    (padding_x + 5 * circle_diameter + circle_radius, 
                                    padding_y + 2 * circle_diameter + circle_radius), 3)
    
    pygame.draw.line(screen, mau_vien, (padding_x + 5 * circle_diameter + circle_radius, 
                                     padding_y + 0 * circle_diameter + circle_radius), 
                                    (padding_x + 3 * circle_diameter + circle_radius, 
                                    padding_y + 2 * circle_diameter + circle_radius), 3)

# Vẽ quân cờ
def draw_piece(x, y, piece_text, selected = False):
    if selected:
        pygame.draw.circle(screen, RED, (x, y), circle_radius - 10)

    # Vẽ vòng tròn ngoài
    pygame.draw.circle(screen, quan_co, (x, y), circle_radius - 10, 1)

    # Vẽ vòng tròn với màu sắc của quân cờ dựa trên đội
    pygame.draw.circle(screen, quan_co, (x, y), circle_radius - 10 - 2)  # Vẽ vòng tròn màu trắng cho quân cờ đội xanh

    # Hiển thị văn bản đại diện cho quân cờ với phông chữ và kích thước phù hợp
    font = pygame.font.Font(font_path, 60)
    if piece_text in red_team:
        text = font.render(piece_text, True, RED)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    elif piece_text in blue_team:
        text = font.render(piece_text, True, BLACK)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    
def draw_pieces(board):
    for row in range(10):
        for col in range(9):
            if board[row][col] is not None:
                selected = (row, col) 
                draw_piece(padding_x + col * circle_diameter + circle_radius,
                           padding_y + row * circle_diameter + circle_radius, 
                           board[row][col], selected)

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
red_team =  ["車" , "馬", "相", "士", "将", "砲", "卒"]
blue_team = ["俥", "傌", "象", "仕", "帥", "炮", "兵"]


selected_pos = None
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


def expect_move(selected_piece, selected_pos, board_move):
    box = []
    cannoe_eat = []
    for a in range(10):
        for b in range(9):
            move_ = Move(a, b, selected_piece, selected_pos, board_move)
            c = (selected_piece in blue_team) and (board_move[a][b] is None or board_move[a][b] in red_team)
            d = (selected_piece in red_team)  and (board_move[a][b] is None or board_move[a][b] in blue_team)
            if (c or d):
                if selected_piece in ["卒", "兵"]:
                    if move_.pawn():
                        box.append((a, b))
                elif selected_piece in ["砲", "炮"]:
                    if move_.gun():
                        if isinstance(move_.gun(), list):
                            box.append((a, b))
                            if move_.gun()[1] == "eat":
                                cannoe_eat.append((a, b))
                elif selected_piece in ["車", "俥"]:
                    if move_.car():
                        box.append((a, b))
                elif selected_piece in ["馬", "傌"]:
                    if move_.horse():
                        box.append((a, b))
                elif selected_piece in ["相", "象"]:
                    if move_.elephant():
                        box.append((a, b))
                elif selected_piece in ["士", "仕"]:
                    if move_.body_guard():
                        box.append((a, b))
                elif selected_piece in ["将", "帥"]:
                    if move_.king():
                        box.append((a, b))
    return box, cannoe_eat

def protect_king(king, id_king, board_ảo):
    box_1 = []
    if king == "将":
        for a in range(10):
            for b in range(9):
                if board_ảo[a][b] in blue_team:
                    if board_ảo[a][b] not in ['砲', "炮"]:
                        box_1.append(expect_move(board_ảo[a][b], (a, b), board_ảo)[0])
                    elif board_ảo[a][b]  == "炮":
                        eat = expect_move(board_ảo[a][b], (a, b), board_ảo)[1]
                        box_1.append(eat)
                        
    if king == "帥":
        for a in range(10):
            for b in range(9):
                if board_ảo[a][b] in red_team and board_ảo[a][b] not in ['砲', "炮"]:
                    box_1.append(expect_move(board_ảo[a][b], (a, b), board_ảo)[0])
                elif board_ảo[a][b] in blue_team and board_ảo[a][b]  == '砲':
                    eat = expect_move(board_ảo[a][b], (a, b), board_ảo)[1]
                    box_1.append(eat)
                    
    check_1 = any(id_king in sublist for sublist in box_1)    
    if check_1:
        return False
    else:
        return True
    

@dataclass
class SoundManager:
    def __init__(self):
        self.eat_sound: pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\đớp-mồi.wav")
        self.nervous_sound: pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\gây cấn (mp3cut (mp3cut.net).mp3")
        self.intro_sound :  pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\intro.wav")
        self.move_trong : pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\move-trống.wav")
        self.danh_kiem_sound : pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\ăn-đánh-kiếm.wav")
        self.current_channel = None
        
    def eat(self):
        self.eat_sound.play()
        
    def play_nervous(self):
        if self.current_channel is None:
            # self.current_channel.stop()
            self.current_channel = pygame.mixer.find_channel()
            self.current_channel.play(self.nervous_sound, loops=-1)

    def stop_nervous(self):
        if self.current_channel is not None:
            self.current_channel.stop()
            self.current_channel = None
        
    def intro(self):
        self.intro_sound.play()
        
    def move(self):
        self.move_trong.play()
        
    def danh_kiem(self):
        self.danh_kiem_sound.play()
sound_manager = SoundManager()
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
                                row, col = c
                                board_ảo = copy.deepcopy(board)
                                board_ảo[selected_pos[0]][selected_pos[1]] = None
                                board_ảo[row][col] = selected_piece
                                board_array = np.array(board_ảo)
                                position = np.where(board_array == "将")
                                formatted_position = (position[0][0], position[1][0])
                                if protect_king("将", formatted_position, board_ảo):
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
                        # print(selected_piece, box)
                        for c in box:
                                row, col = c
                                board_ảo[selected_pos[0]][selected_pos[1]] = None
                                board_ảo[row][col] = selected_piece
                                board_array = np.array(board_ảo)
                                position_blue = np.where(board_array == "帥")
                                formatted_position_blue = (position_blue[0][0], position_blue[1][0])
                                
                                if protect_king("帥", formatted_position_blue, board_ảo):
                                    flat = True
                                    winner = None
                                    break
                if flat:
                    break                
    return flat, winner

def gay_can(team, board):
    if team == 'red': # thủ
        count = 0
        for a in range(10):
            for b in range(9):
                if board[a][b] is not None:
                    if a >= 6 and board[a][b] in red_team:
                        count += 1
                        if count >= 4:
                            return True
    if team == 'blue': # thủ
        count = 0
        for a in range(10):
            for b in range(9):
                if board[a][b] is not None:
                    if a <= 3 and board[a][b] in blue_team:
                        count += 1
                        if count >= 4:
                            return True
    return False


# tạo danh sách red team > 
def rule_move(selected_piece, selected_pos, board_move_1):
    rule = expect_move(selected_piece, selected_pos, board_move_1)
    board_move_2 = copy.deepcopy(board_move_1)
    for a in rule[0]:
        row = a[0]
        col = a[1]
        board_move_2[row][col] = "x"  
    return board_move_2

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