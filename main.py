import random

def main():
    print("Hello from chess-in-cli!\n")
    grid(piece="", from_pos="", to_pos="")
    piece, from_pos, to_pos = userInput()
    # print(f"✅ Move to make in the board: {piece} from {from_pos} to {to_pos}")
    grid(piece, from_pos, to_pos)

# Next step:
# - [ ] Make the piece move according to the inputs received from the user

def userInput(): 
  print("\n")
  print("Format: piece-from-to")
  move = input("Your move: ").strip()

  if move.count("-") != 2:
      print("❌ Invalid format. Use: piece-from-to (e.g., wRr-h2-h4)")
      return None
  
  piece, from_pos, to_pos = move.split("-")
  # print(f"✅ Parsed move: {piece} from {from_pos} to {to_pos}")
  return piece, from_pos, to_pos

def grid(piece, from_pos, to_pos):
  board = white_board_dict if choice == "white" else black_board_dict

  if piece and from_pos and to_pos:
      if board[from_pos] != piece:
        print(f"❌ {piece} not found at {from_pos}")
      else:
        board[to_pos] = piece
        board[from_pos] = "-*-"

  print(f"choice: {choice}\n")
  print_board(board)


   
mylist = ["black", "white"]

choice = random.choice(mylist)

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = ["8", "7", "6", "5", "4", "3", "2", "1"]

white_board_dict = {}
black_board_dict = {}

white_setup = [
    ["bRl", "bNl", "bBl", "bK ", "bQ ", "bBr", "bNr", "bRr"],  # 8
    ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],  # 7
    ["-*-"] * 8,  # 6
    ["-*-"] * 8,  # 5
    ["-*-"] * 8,  # 4
    ["-*-"] * 8,  # 3
    ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],  # 2
    ["wRl", "wNl", "wBl", "wK ",  "wQ ",  "wBr", "wNr", "wRr"]   # 1
]

black_setup = [
    ["wRl", "wNl", "wBl", "wK ",  "wQ ",  "wBr", "wNr", "wRr"],  # 8
    ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],  # 7
    ["-*-"] * 8,  # 6
    ["-*-"] * 8,  # 5
    ["-*-"] * 8,  # 4
    ["-*-"] * 8,  # 3
    ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],  # 2
    ["bRl", "bNl", "bBl", "bK ",  "bQ ",  "bBr", "bNr", "bRr"]   # 1
]

for row in range(8):
   for col in range(8):
      pos = files[col] + ranks[row]
      white_board_dict[pos] = white_setup[row][col]
      black_board_dict[pos] = black_setup[row][col]

def print_board(board_dict):
  for r in ranks:
      row = []
      for f in files:
         cell = f + r
         row.append(board_dict[cell])
      print(f"{r} " + " ".join(row))
  print("  " + "  ".join(files))



if __name__ == "__main__":
   # - [ ] Need to keep the game running
   while True:
    main()
