import random
import os
import chess
import chess.engine

engine_path = "/opt/homebrew/bin/stockfish"  
engine = chess.engine.SimpleEngine.popen_uci(engine_path)
board = chess.Board()

def get_computer_move():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    return result.move.uci() 

mylist = ["black", "white"]

# choice = random.choice(mylist)
piece = ""
from_pos = "" 
to_pos = ""

def get_game_type():
   print("Press 0 for Computer")
   print("Press 1 for Human")
   game_type = input("Select Game Type: ")
   return game_type

# - [ ] take this from the user
# get_game_type_result = get_game_type()
get_game_type_result = "1"

if get_game_type_result == "0":
   game_type = "computer"
elif get_game_type_result == "1":
   game_type = "human"
else:
   game_type = "unknown"


def main():
  if game_type == "human":
     print("It's human vs human")
     turn = "white"
     
     grid("", "", "", turn)

     for _ in range(100):
      piece, from_pos, to_pos = userInput()
      grid(piece, from_pos, to_pos, turn)
      turn = "black" if turn == "white" else "white"
  else:
     print("Computer mode not implemented yet.")


# Next step:

# - [x] get the type of game from user (vs computer or vs human)
# - [x] Need to keep the game running
# - [x] Make the piece move according to the inputs received from the user
# - [x] Make the grid change in place. And not have to draw the grid again.
# - [ ] The board should be displayed according to who's move it is (black / white)
  # currently we are displayiing the board based on the random choice
  # ? Does this board view persists over all the loops
  # A: Yes it does
  # ? We need to decide who's move it is
  # Because white is what always makes the first move
  # All we need to do is to set the white to the user/computer (human vs computer)
  # And in human vs human we need to set it to any of the human
  # ? We need to pass the move control from one player to another (in both cases)

# fixes

# - [ ] Even wrongs moves are also showing as successful but are not affecting the board 


def userInput(): 
  global piece, from_pos, to_pos
  print("\n")
  if piece and from_pos and to_pos:
    print(f"✅ Your previous move: {piece} from {from_pos} to {to_pos}")
  print("Format: piece-from-to")
  move = input("Your move: ").strip()

  if move.count("-") != 2:
      print("❌ Invalid format. Use: piece-from-to (e.g., wRr-h2-h4)")
      return None
  
  piece, from_pos, to_pos = move.split("-")
  return piece, from_pos, to_pos

def grid(piece, from_pos, to_pos, turn):
  board = white_board_dict

  if piece and from_pos and to_pos:
      if board[from_pos] != piece:
        print(f"❌ {piece} not found at {from_pos}")
      else:
        board[to_pos] = piece
        board[from_pos] = "---"

  flip = (turn == "black") 
  print_board(board, flip)


   
files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = ["8", "7", "6", "5", "4", "3", "2", "1"]

white_board_dict = {}
black_board_dict = {}

white_setup = [
    ["bRl", "bNl", "bBl", "bK", "bQ", "bBr", "bNr", "bRr"],  # 8
    ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],  # 7
    # ["⬜"] * 8, # 6
    # ["⬜"] * 8, # 5
    # ["⬜"] * 8, # 4
    # ["⬜"] * 8, # 3
    ["---"] * 8,
    ["---"] * 8,
    ["---"] * 8,
    ["---"] * 8,
    ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],  # 2
    ["wRl", "wNl", "wBl", "wK ",  "wQ ",  "wBr", "wNr", "wRr"]   # 1
]

black_setup = [
    ["wRl", "wNl", "wBl", "wK",  "wQ",  "wBr", "wNr", "wRr"],  # 8
    ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],  # 7
    # ["⬜"] * 8, # 6
    # ["⬜"] * 8, # 5
    # ["⬜"] * 8, # 4
    # ["⬜"] * 8, # 3
    ["---"] * 8,
    ["---"] * 8,
    ["---"] * 8,
    ["---"] * 8,
    ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],  # 2
    ["bRl", "bNl", "bBl", "bK",  "bQ",  "bBr", "bNr", "bRr"]   # 1
]

for row in range(8):
   for col in range(8):
      pos = files[col] + ranks[row]
      white_board_dict[pos] = white_setup[row][col]
      black_board_dict[pos] = black_setup[row][col]

def normalize(cell, width=5):
   return cell.center(width)

def print_board(board_dict, flip):
  os.system('clear')
  term_width = os.get_terminal_size().columns
  board_lines = []

  row_ranks = ranks[::-1] if not flip else ranks[:]
  col_files = files[:] if not flip else files[::-1]

  for r in row_ranks:
      row = []
      for f in col_files:
         cell = f + r
         row.append(normalize(board_dict[cell]))
      # content_line = f"{r} " + " ".join(row)
      display_rank = r if not flip else str(9 - int(r))
      content_line = f"{display_rank} " + " ".join(row)
      spacer_line = "  " + " ".join([" " * 5] * 8) 
      board_lines.append(content_line)
      board_lines.append(spacer_line)
    
  footer = "   " + "".join(f.center(6) for f in files)
  board_lines.append(footer)

  for line in board_lines:
     padding = (term_width - len(line)) // 2
     print(" " * max(padding, 0) + line)


if __name__ == "__main__":
   main()  

