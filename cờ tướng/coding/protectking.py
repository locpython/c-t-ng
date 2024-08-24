from abletomove import expect_move
from frontend import blue_team, red_team
import copy
import numpy as np

def kings_seeing(board):
    id_king_red = np.where(board == "将")
    id_king_blue = np.where(board == "帥")
    if len(id_king_red[0]) == 0 or len(id_king_blue[0]) == 0:
        return False  # Nếu không tìm thấy tướng đỏ hoặc tướng xanh, trả về False

    king_red_pos = (id_king_red[0][0], id_king_red[1][0])
    king_blue_pos = (id_king_blue[0][0], id_king_blue[1][0])
    
    if king_red_pos[1] == king_blue_pos[1]:  # Cùng cột
        col = king_red_pos[1]
        row_start = min(king_red_pos[0], king_blue_pos[0])
        row_end = max(king_red_pos[0], king_blue_pos[0])
        # Kiểm tra có quân cờ nào cản trở giữa hai quân tướng không
        for row in range(row_start + 1, row_end):
            if board[row][col] != None:
                # print(1)
                return False
        # print(2)
        return True
    # print(3)
    return False  # Không nằm trên cùng một hàng hoặc cột

def protect_king(king, board_ảo, plan, selected_pos, selected_piece):
  row, col = plan
  board_ảo = np.array(copy.deepcopy(board_ảo))
  
  board_ảo[selected_pos[0]][selected_pos[1]] = None # chọn
  board_ảo[row][col] = selected_piece
  position = np.where(board_ảo == king)
  id_king = (position[0][0], position[1][0]) 
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

                      #"将","帥"
  if king == "帥":
      for a in range(10):
          for b in range(9):
              if board_ảo[a][b] in red_team:
                if board_ảo[a][b] not in ['砲', "炮"]:
                    box_1.append(expect_move(board_ảo[a][b], (a, b), board_ảo)[0])
                elif board_ảo[a][b]  == '砲':
                    eat = expect_move(board_ảo[a][b], (a, b), board_ảo)[1]
                    # print(eat)
                    box_1.append(eat)
                  
  check_1 = any(id_king in sublist for sublist in box_1)   
  if check_1 == False and kings_seeing(board_ảo) == False:
      return True
#   return False