from valid_to_go import check_army
import math


def hàm_tính_khoảng_cách_con_chuột(x, y, padding_x, padding_y, circle_diameter, circle_radius, board):
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
              box = check_army(selected_piece, board, selected_pos)[(selected_piece,selected_pos)]
              print(box)
              step = 1
              return selected_piece, selected_pos, box, step
          else:
              return 1, 1, 2, 0 # quan trọng là step == 0
      else:
              return 1, 1, 2, 0 # quan trọng là step == 0
  else:
        return 1, 1, 2, 0 # quan trọng là step == 0
# for piece_dict in valid_all_board(board, 'red'):
#     for (label, position), moves in piece_dict.items():
#         # Print piece label, position, and its valid moves
#         print(f"Piece: {label} at position {position}")
#         for move in moves:
#           print(f"  Valid move:   {move}")