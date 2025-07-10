from board import create_board, print_board

move = "white"

if __name__ == "__main__":
  board = create_board()

  while True:
    print("\n--- White's View ---")
    print_board(board, flip=False)

    # print("\n--- Black's View ---")
    # print_board(board, flip=True)

    print("\n")
    print("input format: a2a4 (a2: from cell, a4: to cell)")
    user_input = input(f"{move}'s move: ")
    print("\n")
    print("user_input: ", user_input)
    from_cell, to_cell = user_input[:2], user_input[2:] 
    print("from_cell: ", from_cell, "to_cell: ", to_cell)

    # update the board with user move
    board[to_cell] = board[from_cell]
    board[from_cell] = "---"

    move = "black" if  move == "white" else "white"

  


