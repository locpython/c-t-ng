import pygame as p
import time
import math

# Initialize Pygame
p.init()

class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ''
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x_val, y_val):
      global turn, won
      if self.content == '':
          if self.rect.collidepoint(x_val, y_val):
              self.content = turn
              board[self.number] = turn

              if turn == 'x':
                  self.image = x_image
                  self.image = p.transform.scale(self.image, (self.width, self.height))
                  turn = 'o'
                  check_winner('x')  # Gọi hàm đúng tên

                  if not won:
                      comp_move()

              else:
                  self.image = o_image
                  self.image = p.transform.scale(self.image, (self.width, self.height))
                  turn = 'x'
                  check_winner('o')  # Gọi hàm đúng tên



def check_winner(player):
    global background, won, startX, startY, endX, endY

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
            won = True
            get_pos(winners[i][0], winners[i][2])
            break

    if won:
        update_display()
        draw_line(startX, startY, endX, endY)

        square_group.empty()
        background = p.image.load(player.upper() + ' Wins.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))

def get_pos(n1, n2):
    global startX, startY, endX, endY

    for sqs in squares:
        if sqs.number == n1:
            startX = sqs.x
            startY = sqs.y
        elif sqs.number == n2:
            endX = sqs.x
            endY = sqs.y

def draw_line(x1, y1, x2, y2):
    p.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 15)
    p.display.update()
    time.sleep(2)

def update_display():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()

def minimax(board, depth, alpha, beta, maximizing):
    if check_terminal_state(board):
        return evaluate_board(board)
    
    valid_moves = [i for i in range(1, 10) if board[i] == '']
    if maximizing:
        max_eval = -math.inf
        for move in valid_moves:
            board[move] = 'o'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = ''
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in valid_moves:
            board[move] = 'x'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = ''
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate_board(board):
    for i in range(8):
        if board[winners[i][0]] == board[winners[i][1]] == board[winners[i][2]] != '':
            if board[winners[i][0]] == 'o':
                return 10
            elif board[winners[i][0]] == 'x':
                return -10
    return 0

def check_terminal_state(board):
    for player in ['x', 'o']:
        if any(board[winners[i][0]] == board[winners[i][1]] == board[winners[i][2]] == player for i in range(8)):
            return True
    return all(cell != '' for cell in board[1:])

def comp_move():
    global move, background

    best_move = None
    best_value = -math.inf
    valid_moves = [i for i in range(1, 10) if board[i] == '']

    for move in valid_moves:
        board[move] = 'o'
        move_value = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = ''
        if move_value > best_value:
            best_value = move_value
            best_move = move

    if best_move is not None:
        for square in squares:
            if square.number == best_move:
                square.clicked(square.x, square.y)
                break
    else:
        update_display()
        time.sleep(1)
        square_group.empty()
        background = p.image.load('Tie Game.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))

WIDTH = 500
HEIGHT = 500

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Tic Tac Toe')
clock = p.time.Clock()

blank_image = p.image.load('Blank.png')
x_image = p.image.load('x.png')
o_image = p.image.load('o.png')
background = p.image.load('Background.png')

background = p.transform.scale(background, (WIDTH, HEIGHT))

move = True
won = False
compMove = 5

square_group = p.sprite.Group()
squares = []

winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = ['' for i in range(10)]

startX = 0
startY = 0
endX = 0
endY = 0

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)
        num += 1

turn = 'x'
run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        if event.type == p.MOUSEBUTTONDOWN and turn == 'x':
            mx, my = p.mouse.get_pos()
            for s in squares:
                s.clicked(mx, my)

    update_display()

p.quit()
