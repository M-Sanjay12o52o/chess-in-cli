import random

def main():
    print("Hello from chess-in-cli!\n")
    grid()
    userInput()

def userInput(): 
  print("Enter your move on the format: piece-from-to")
  print("Example: wRr-h2-h4 (White Root Right - from h2 - to h4")
  move = input("Your move: ").strip()

  if move.count("-") != 2:
      print("❌ Invalid format. Use: piece-from-to (e.g., wRr-h2-h4)")
      return None
  
  piece, from_pos, to_pos = move.split("-")
  print(f"✅ Parsed move: {piece} from {from_pos} to {to_pos}")
  return piece, from_pos, to_pos

def grid():
  if choice == "white":
      print("choice: ", choice)
      print("\n")
      for row in white_board:
          print(row)
  elif choice == "black":
      print("choice: ", choice)
      print("\n")
      for row in black_board:
          print(row)
    
mylist = ["black", "white"]

choice = random.choice(mylist)

white_board = [
    "8  bRl  bNl  bBl  bK   bQ   bBr  bNr  bRr",
    "7  bp1  bp2  bp3  bp4  bp5  bp6  bp7  bp8",
    "6  -*-  -*-  -*-  -*-  -*-  -*-  -*-  -*-",
    "5  -*-  -*-  -*-  -*-  -*-  -*-  -*-  -*-",
    "4  -*-  -*-  -*-  -*-  -*-  -*-  -*-  -*-",
    "3  -*-  -*-  -*-  -*-  -*-  -*-  -*-  -*-",
    "2  wp1  wp2  wp3  wp4  wp5  wp6  wp7  wp8",
    "1  wRl  wNl  wBl  wK   wQ   wBr  wNr  wRr",
    "    a    b    c    d    e    f    g    h",
]

black_board = [
    "8  wRl wNl wBl wK  wQ  wBr wNr wRr",
    "7  wp1 wp2 wp3 wp4 wp5 wp6 wp7 wp8",
    "6  -*- -*- -*- -*- -*- -*- -*- -*-",
    "5  -*- -*- -*- -*- -*- -*- -*- -*-",
    "4  -*- -*- -*- -*- -*- -*- -*- -*-",
    "3  -*- -*- -*- -*- -*- -*- -*- -*-",
    "2  bp1 bp2 bp3 bp4 bp5 bp6 bp7 bp8",
    "1  bRl bNl bBl bK  bQ  bBr bNr bRr",
    "    a   b   c   d   e   f   g   h"
]



if __name__ == "__main__":
    main()
