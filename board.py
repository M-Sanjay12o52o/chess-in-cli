import shutil
from utils import get_piece_symbol

# features
# - [ ] have it centered in view in the terminal
# - [ ] i am trying to increase the size of the board 

# fixes
# - [ ] reverse the pawns (it should be white in place of black and black in place of white)

def center_line(line):
    width = shutil.get_terminal_size().columns
    return line.center(width)

def create_board():
    board = {}

    # Files and ranks
    files = "abcdefgh"
    # ranks = "12345678"

    # Set up white pieces
    white_pieces = ["wRl", "wNl", "wBl", "wQ ", "wK ", "wBr", "wNr", "wRr"]
    for i, file in enumerate(files):
        board[file + "1"] = white_pieces[i]
        board[file + "2"] = f"wp{i+1}"

    # Set up black pieces
    black_pieces = ["bRl", "bNl", "bBl", "bQ ", "bK ", "bBr", "bNr", "bRr"]
    for i, file in enumerate(files):
        board[file + "8"] = black_pieces[i]
        board[file + "7"] = f"bp{i+1}"

    # Empty squares
    for rank in "3456":
        for file in files:
            board[file + rank] = "---"

    return board


def print_board(board, flip=False):
    files = "abcdefgh"
    ranks = "12345678"
    if flip:
        files = files[::-1]
        ranks = ranks
    else:
        ranks = ranks[::-1]

    for rank in ranks:
        row = [get_piece_symbol(board[file + rank]) for file in files]
        spaced_row = "   ".join(row)
        line = f"{rank}   {spaced_row}"
        print(center_line(line))
    file_labels = "   ".join(files if not flip else files[::-1])
    print(center_line("    " + file_labels))


if __name__ == "__main__":
    board = create_board()
    print("\n--- White's View ---")
    print_board(board, flip=False)
    print("\n--- Black's View ---")
    print_board(board, flip=True)