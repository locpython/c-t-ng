import pygame

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

red_team =  ["車" , "馬", "相", "士", "将", "砲", "卒"]
blue_team = ["俥", "傌", "象", "仕", "帥", "炮", "兵"]