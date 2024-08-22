from abletomove import expect_move
from frontend import blue_team, red_team


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