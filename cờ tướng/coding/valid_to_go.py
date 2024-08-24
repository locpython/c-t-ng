from protectking import protect_king, red_team, blue_team
from copy import deepcopy
from abletomove import expect_move
from protectking import protect_king

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

def check_army(army_type, board, selected_pos):
    valid = {(army_type, selected_pos) :[]}  # Khởi tạo dictionary với loại quân cờ và danh sách nước đi hợp lệ
    board_ảo = deepcopy(board)
    
    # Giả sử expect_move trả về danh sách các nước đi khả thi cho quân cờ
    box = expect_move(army_type, selected_pos, board_ảo)[0]
    
    for plan in box:  # plan có dạng (row, col)
        # Kiểm tra nếu quân cờ thuộc đội đỏ
        if army_type in red_team and protect_king("将", board_ảo, plan, selected_pos, army_type):
            valid[army_type, selected_pos].append(plan)
        
        # Kiểm tra nếu quân cờ thuộc đội xanh
        if army_type in blue_team and protect_king("帥", board_ảo, plan, selected_pos, army_type):
            valid[army_type, selected_pos].append(plan)
    
    return valid

def valid_all_board(board, team):
    board_new = deepcopy(board)
    valid = []
    if team == 'blue':
        for row in range(10):
            for col in range(9):
                if board_new[row][col] in blue_team:
                    piece = board_new[row][col]
                    valid_moves = check_army(piece, board_new, (row, col))
                    valid.append(valid_moves)  # Combine results into a single dictionary

    if team == 'red':
        for row in range(10):
            for col in range(9):
                if board_new[row][col] in red_team:
                    piece = board_new[row][col]
                    valid_moves = check_army(piece, board_new, (row, col))
                    valid.append(valid_moves)  # Combine results into a single dictionary
    return valid
