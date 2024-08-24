from rule_move import Move
red_team =  ["車" , "馬", "相", "士", "将", "砲", "卒"]
blue_team = ["俥", "傌", "象", "仕", "帥", "炮", "兵"]

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
                        if isinstance(move_.gun(), list): #True k phải list là False
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
