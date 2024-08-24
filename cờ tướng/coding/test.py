from frontend import red_team, blue_team
import numpy as np
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
        return values_red.get(piece, 0)**3 
    if piece in blue_team:
        return values_blue.get(piece, 0)**3
    return 0

def flatten_board(board):
    flattened_board = []
    for row in board:
        for cell in row:
            # Mã hóa quân cờ thành số (hoặc có thể sử dụng một cách mã hóa khác)
            value = piece_value(cell)
            flattened_board.append(value)
    return np.array(flattened_board)

# Bảng cờ
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

print(flatten_board(board))
