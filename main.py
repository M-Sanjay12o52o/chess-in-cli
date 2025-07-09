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
computer_move = get_computer_move()

choice = random.choice(mylist)
piece = ""
from_pos = "" 
to_pos = ""

def main():
    for i in range(100):
      if i == 0:
        print("Hello from chess-in-cli!\n")
        grid(piece="", from_pos="", to_pos="")
      piece, from_pos, to_pos = userInput()
      grid(piece, from_pos, to_pos)

# Next step:
# - [x] Need to keep the game running
# - [x] Make the piece move according to the inputs received from the user
# - [ ] The board should be displayed according to who's move it is (black / white)
# - [x] Make the grid change in place. And not have to draw the grid again.

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

def grid(piece, from_pos, to_pos):
  board = white_board_dict if choice == "white" else black_board_dict

  if piece and from_pos and to_pos:
      if board[from_pos] != piece:
        print(f"❌ {piece} not found at {from_pos}")
      else:
        board[to_pos] = piece
        board[from_pos] = "---"

  print(f"choice: {choice}\n")
  print_board(board)


   
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

def print_board(board_dict):
  os.system('clear')
  print(f"{choice}'s move")
  print("computer_move: ", computer_move)
  term_width = os.get_terminal_size().columns
  board_lines = []

  for r in ranks:
      row = []
      for f in files:
         cell = f + r
         row.append(normalize(board_dict[cell]))
      content_line = f"{r} " + " ".join(row)
      spacer_line = "  " + " ".join([" " * 5] * 8) 
      board_lines.append(content_line)
      board_lines.append(spacer_line)
    
  footer = "   " + "".join(f.center(6) for f in files)
  board_lines.append(footer)

  for line in board_lines:
     padding = (term_width - len(line)) // 2
     print(" " * max(padding, 0) + line)


if __name__ == "__main__":
  print("Hello from chess-in-cli!\n")
  grid("", "", "")
  for _ in range(100):
    piece, from_pos, to_pos = userInput()
    grid(piece, from_pos, to_pos)


