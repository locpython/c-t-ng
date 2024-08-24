from abletomove import red_team, blue_team
import math

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

def table_piece(selected_piece, row, col):
    def rotate_table(table):
        return [row[::-1] for row in table[::-1]]
    
    if selected_piece in blue_team:
        is_blue_team = True
    else:
        is_blue_team = False
        
    if selected_piece in ["将", "帥"]:
        King_table = [
            [0, 0, 0, 10, 50, 10, 0, 0, 0],
            [0, 0, 0, -20, -10, -20, 0, 0, 0],
            [0, 0, 0, -30, -30, -30, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        if is_blue_team:
            King_table = rotate_table(King_table)
        return King_table[row][col]

    if selected_piece in ["士", "仕"]:
        body_guard_table = [
            [0, 0, 0, 20, 0, 20, 0, 0, 0],
            [0, 0, 0, 0, 30, 0, 0, 0, 0],
            [0, 0, 0, 10, 0, 10, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        if is_blue_team:
            body_guard_table = rotate_table(body_guard_table)
        return body_guard_table[row][col]

    if selected_piece in ["相", "象"]:
        elephant_table = [
            [0, 0, 20, 0, 0, 0, 20, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [10, 0, 0, 0, 30, 0, 0, 0, 10],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 10, 0, 0, 0, 10, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        if is_blue_team:
            elephant_table = rotate_table(elephant_table)
        return elephant_table[row][col]

    if selected_piece in ["卒", "兵"]:
        Pawn_table = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -2, 0, 4, 0, -2, 0, 0],
            [2, 0, 8, 0, 8, 0, 8, 0, 2],
            [6, 12, 18, 18, 20, 18, 18, 12, 6],
            [10, 20, 30, 34, 40, 34, 30, 20, 10],
            [14, 26, 42, 60, 80, 60, 42, 26, 14],
            [18, 36, 56, 80, 120, 80, 56, 36, 18],
            [0, 3, 6, 9, 12, 9, 6, 3, 0],
        ]
        if is_blue_team:
            Pawn_table = rotate_table(Pawn_table)
        return Pawn_table[row][col]

    if selected_piece in ["馬", "傌"]:
        horse_table = [
            [0, -4, 0, 0, 0, 0, 0, -4, 0],
            [0, 2, 4, 4, -2, 4, 4, 2, 0],
            [4, 2, 8, 8, 4, 8, 8, 2, 4],
            [2, 6, 8, 6, 10, 6, 8, 6, 2],
            [4, 12, 16, 14, 12, 14, 16, 12, 4],
            [6, 16, 14, 18, 16, 18, 14, 16, 6],
            [8, 24, 18, 24, 20, 24, 18, 24, 8],
            [12, 14, 16, 20, 18, 20, 16, 14, 12],
            [4, 10, 28, 16, 8, 16, 28, 10, 4],
            [4, 8, 16, 12, 4, 12, 16, 8, 4],
        ]
        if is_blue_team:
            horse_table = rotate_table(horse_table)
        return horse_table[row][col]

    if selected_piece in ["車", "俥"]:
        Car_table = [
            [-2, 10, 6, 14, 12, 14, 6, 10, -2],
            [8, 4, 8, 16, 8, 16, 8, 4, 8],
            [4, 8, 6, 14, 12, 14, 6, 8, 4],
            [6, 10, 8, 14, 14, 14, 8, 10, 6],
            [12, 16, 14, 20, 20, 20, 14, 16, 12],
            [12, 14, 12, 18, 18, 18, 12, 14, 12],
            [12, 18, 16, 22, 22, 22, 16, 18, 12],
            [12, 12, 12, 18, 18, 18, 12, 12, 12],
            [16, 20, 18, 24, 26, 24, 18, 20, 16],
            [14, 14, 12, 18, 16, 18, 12, 14, 14],
        ]
        if is_blue_team:
            Car_table = rotate_table(Car_table)
        return Car_table[row][col]

    if selected_piece in ["砲", "炮"]:
        gun_table = [
            [0, 0, 2, 6, 6, 6, 2, 0, 0],
            [0, 2, 4, 6, 6, 6, 4, 2, 0],
            [4, 0, 8, 6, 10, 6, 8, 0, 4],
            [0, 0, 0, 2, 4, 2, 0, 0, 0],
            [-2, 0, 4, 2, 6, 2, 4, 0, -2],
            [2, 0, 4, 2, 6, 2, 4, 0, 2],
            [0, 2, 2, 2, 4, 2, 2, 2, 0],
            [2, 4, 4, 6, 10, 6, 4, 4, 2],
            [4, 8, 6, 10, 12, 10, 6, 8, 4],
            [0, 0, 2, 6, 6, 6, 2, 0, 0],
        ]
        if is_blue_team:
            gun_table = rotate_table(gun_table)
        return gun_table[row][col]

from copy import deepcopy
# Hàm tính điểm vị trí của bàn cờ
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

def piece_value(piece):
    # Assign values to each type of piece
    
    values_red = {
        '将': 10000,  # King
        '士': 20,   # Bodyguard
        '相': 20,   # Elephant
        '馬': 40,   # Horse
        '車': 90,   # Car (Chariot)
        '砲': 45,   # Gun (Cannon)
        '卒': 15,   # Pawn
    }
    values_blue = {
        '帥': 10000,  # King
        '仕': 20,   # Bodyguard
        '象': 20,   # Elephant
        '傌': 30,   # Horse
        '俥': 100,   # Car (Chariot)
        '炮': 35,   # Gun (Cannon)
        '兵': 10,   # Pawn
    }
    if piece in red_team:
        return values_red.get(piece[-1], 0)**3 
    if piece in blue_team:
        return values_blue.get(piece[-1], 0)**3

  
  
def eval_position(board):
    score_AI = 0
    score_me = 0
    for row in range(10):
        for col in range(9):
            piece = board[row][col]
            if piece is not None:
                value = piece_value(piece) + table_piece(piece, row, col)
                if piece in red_team:
                    score_AI += value
                elif piece in blue_team:
                    score_me -= value
    return score_AI + score_me

def flatten_board(board):
    flattened_board = []
    for row in board:
        for cell in row:
            # Mã hóa quân cờ thành số (hoặc có thể sử dụng một cách mã hóa khác)
            value = piece_value(cell)
            flattened_board.append(value)
    return np.array(flattened_board)


from checkwin import check_win
from valid_to_go import valid_all_board

            

def minimax(board, depth, alpha, beta, maximizing_player, model):
    board_certain = deepcopy(board)
    
    red_win, blue_win = check_win('red', board_certain), check_win('blue', board_certain)
     
    if red_win[0]:
        return 10000 + (10 - depth)  # Hoặc giá trị khác tùy theo ưu tiên của bạn
    if blue_win[0]:
        return -10000 - (10 - depth)  # Hoặc giá trị khác tùy theo ưu tiên của bạn
    if depth == 0:  # Điều kiện dừng khi đạt đến độ sâu tối đa
        board_tensor = flatten_board(board_certain)
        evaluation = model(board_tensor).item()
        return evaluation
    
        
    if maximizing_player:
        valid_moves = valid_all_board(board_certain, 'red')  # Get valid moves for 'red'
        max_eval = -math.inf
        for piece_dict in valid_moves.values():  # Iterate through pieces and their valid moves
            for position, moves in piece_dict.items():
                for move in moves:
                    # Make the move
                    board_certain[move[0]][move[1]] = position
                    board_certain[position] = None  # Clear the old position
                    eval = minimax(board_certain, depth - 1, alpha, beta, False)
                    # Undo the move
                    board_certain[position] = board_certain[move[0]][move[1]]
                    board_certain[move[0]][move[1]] = None
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
                if beta <= alpha:
                    break
        return max_eval
    else:
        valid_moves = valid_all_board(board_certain, 'blue')  # Get valid moves for 'blue'
        min_eval = math.inf
        for piece_dict in valid_moves.values():  # Iterate through pieces and their valid moves
            for position, moves in piece_dict.items():
                for move in moves:
                    # Make the move
                    board_certain[move[0]][move[1]] = position
                    board_certain[position] = None  # Clear the old position
                    eval = minimax(board_certain, depth - 1, alpha, beta, True)
                    # Undo the move
                    board_certain[position] = board_certain[move[0]][move[1]]
                    board_certain[move[0]][move[1]] = None
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
                if beta <= alpha:
                    break
        return min_eval
        
def comp_move(board):
    global model
    board_certain = deepcopy(board)
    best_move = None
    best_value = -math.inf
    best_label = None
    best_position = None

    valid_moves = valid_all_board(board, 'red')  # Retrieve valid moves for 'red'

    for piece_dict in valid_moves:  # Iterate through pieces and their valid moves
        for (label, position), moves in piece_dict.items():
            for move in moves:
                # Make the move on a copy of the board
                board_certain[move[0]][move[1]] = label
                board_certain[position[0]][position[1]] = None
                
                # Evaluate the move
                move_value = minimax(board_certain, 20, -math.inf, math.inf, True, model)
                
                # Undo the move
                board_certain[position[0]][position[1]] = label
                board_certain[move[0]][move[1]] = None
                
                # Check if this move is better
                if move_value > best_value:
                    best_value = move_value
                    best_move = move
                    best_label = label
                    best_position = position

    return best_move, best_value, best_label, best_position


class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.tanh = nn.Tanh()  # Output layer with tanh activation

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.tanh(x)  # Apply tanh to output
        return x
model = MLP(input_size=90, hidden_size=128, output_size=1)
print(comp_move(board))


# import torch
# import torch.nn as nn
# import torch.optim as optim
# import numpy as np

# # 1. Define the MLP model
# class MLP(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(MLP, self).__init__()
#         self.fc1 = nn.Linear(input_size, hidden_size)
#         self.relu = nn.ReLU()
#         self.fc2 = nn.Linear(hidden_size, hidden_size)
#         self.fc3 = nn.Linear(hidden_size, output_size)
#         self.tanh = nn.Tanh()  # Output layer with tanh activation

#     def forward(self, x):
#         x = self.fc1(x)
#         x = self.relu(x)
#         x = self.fc2(x)
#         x = self.relu(x)
#         x = self.fc3(x)
#         x = self.tanh(x)  # Apply tanh to output
#         return x

# 2. Implement Minimax Algorithm with Alpha-Beta Pruning
# def minimax(board, depth, alpha, beta, maximizing_player, model):
#     board_certain = deepcopy(board)
    
#     red_win, blue_win = check_win('red', board_certain), check_win('blue', board_certain)
    
#     if red_win[0] or blue_win[0] or depth == 0:  # Check for game end condition
#         board_encoded = [[piece_value.get(piece, 0) for piece in row] for row in board]
#         board_flattened = [item for sublist in board_encoded for item in sublist]
#         board_tensor = torch.FloatTensor(board_flattened).unsqueeze(0)
#         evaluation = model(board_tensor).item()  # Get the evaluation from the MLP
#         return evaluation
    
    
#     valid_moves = get_valid_moves(board, maximizing_player)  # Get valid moves for current player
    
#     if maximizing_player:
#         valid_moves = valid_all_board(board_certain, 'red')  # Get valid moves for 'red'
#         max_eval = -math.inf
#         for piece_dict in valid_moves.values():  # Iterate through pieces and their valid moves
#             for position, moves in piece_dict.items():
#                 for move in moves:
#                     # Make the move
#                     board_certain[move[0]][move[1]] = position
#                     board_certain[position] = None  # Clear the old position
#                     eval = minimax(board_certain, depth - 1, alpha, beta, False)
#                     # Undo the move
#                     board_certain[position] = board_certain[move[0]][move[1]]
#                     board_certain[move[0]][move[1]] = ''
#                     max_eval = max(max_eval, eval)
#                     alpha = max(alpha, eval)
#                     if beta <= alpha:
#                         break
#                 if beta <= alpha:
#                     break
#         return max_eval
#     else:
#         valid_moves = valid_all_board(board_certain, 'blue')  # Get valid moves for 'blue'
#         min_eval = math.inf
#         for piece_dict in valid_moves.values():  # Iterate through pieces and their valid moves
#             for position, moves in piece_dict.items():
#                 for move in moves:
#                     # Make the move
#                     board_certain[move[0]][move[1]] = position
#                     board_certain[position] = ''  # Clear the old position
#                     eval = minimax(board_certain, depth - 1, alpha, beta, True)
#                     # Undo the move
#                     board_certain[position] = board_certain[move[0]][move[1]]
#                     board_certain[move[0]][move[1]] = ''
#                     min_eval = min(min_eval, eval)
#                     beta = min(beta, eval)
#                     if beta <= alpha:
#                         break
#                 if beta <= alpha:
#                     break
#         return min_eval

# 3. Function to get the best move using Minimax and MLP
# def get_best_move(board, depth, model):
#     best_eval = -float('inf')
#     best_move = None
#     valid_moves = get_valid_moves(board, True)  # Get valid moves for the maximizing player (AI)
    
#     for move in valid_moves:
#         new_board = make_move(board, move)
#         eval = minimax(new_board, depth - 1, -float('inf'), float('inf'), False, model)
#         if eval > best_eval:
#             best_eval = eval
#             best_move = move
    
#     return best_move

# # Helper functions
# def is_terminal(board):
    # This function should check if the game has ended (checkmate, draw, etc.)
    # Placeholder implementation
#     return False

# def get_valid_moves(board, maximizing_player):
#     # This function should return a list of valid moves for the current player
#     # Placeholder implementation
#     return []

# def make_move(board, move):
#     # This function should apply a move to the board and return the new board state
#     # Placeholder implementation
#     return board

# # 4. Example usage
# input_size = 90  # For a 9x10 board representation
# hidden_size = 128
# output_size = 1  # Single value output representing evaluation

# model = MLP(input_size, hidden_size, output_size)
# criterion = nn.MSELoss()  # Loss function
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# # Example forward pass (random state)
# state = np.zeros((9, 10))  # Example board state (empty board)
# best_move = get_best_move(state, depth=3, model=model)

# print("Best Move:", best_move)
# Flatten a 2D list into a 1D list
# board_flattened = [item for sublist in board for item in sublist]
# board_tensor = torch.FloatTensor(board_flattened).unsqueeze(0)
# print(board_tensor)
# import torch

# # Encode the board
# board_encoded = [[piece_to_value.get(piece, 0) for piece in row] for row in board]

# # Flatten the board and convert to tensor
# board_flattened = [item for sublist in board_encoded for item in sublist]
# board_tensor = torch.FloatTensor(board_flattened).unsqueeze(0)

# print(board_tensor)















# def minimax(board, depth, alpha, beta, maximizing):
#     # Terminal condition check
#     board_certain = deepcopy(board)
#     red_win, blue_win = check_win('red', board_certain), check_win('blue', board_certain)
#     if red_win[0] or blue_win[0] or depth == 0:  # Check for game end condition
#         return eval_position(board)

#     if maximizing:
#         valid_moves = valid_all_board(board_certain, 'red')  # Get valid moves for 'red'
#         max_eval = -math.inf
#         for piece_dict in valid_moves.values():  # Iterate through pieces and their valid moves
#             for position, moves in piece_dict.items():
#                 for move in moves:
#                     # Make the move
#                     board_certain[move[0]][move[1]] = position
#                     board_certain[position] = ''  # Clear the old position
#                     eval = minimax(board_certain, depth - 1, alpha, beta, False)
#                     # Undo the move
#                     board_certain[position] = board_certain[move[0]][move[1]]
#                     board_certain[move[0]][move[1]] = ''
#                     max_eval = max(max_eval, eval)
#                     alpha = max(alpha, eval)
#                     if beta <= alpha:
#                         break
#                 if beta <= alpha:
#                     break
#         return max_eval
#     else:
#         valid_moves = valid_all_board(board_certain, 'blue')  # Get valid moves for 'blue'
#         min_eval = math.inf
#         for piece_dict in valid_moves.values():  # Iterate through pieces and their valid moves
#             for position, moves in piece_dict.items():
#                 for move in moves:
#                     # Make the move
#                     board_certain[move[0]][move[1]] = position
#                     board_certain[position] = ''  # Clear the old position
#                     eval = minimax(board_certain, depth - 1, alpha, beta, True)
#                     # Undo the move
#                     board_certain[position] = board_certain[move[0]][move[1]]
#                     board_certain[move[0]][move[1]] = ''
#                     min_eval = min(min_eval, eval)
#                     beta = min(beta, eval)
#                     if beta <= alpha:
#                         break
#                 if beta <= alpha:
#                     break
#         return min_eval
# 1. Define the MLP model

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

def flatten_board(board):
    flattened_board = []
    for row in board:
        for cell in row:
            # Mã hóa quân cờ thành số (hoặc có thể sử dụng một cách mã hóa khác)
            piece_value = piece_value(cell)
            flattened_board.append(piece_value)
    return np.array(flattened_board)