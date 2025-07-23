from game_loop import play_game

# Add this import for the GUI
try:
    from gui import main as gui_main
except ImportError:
    gui_main = None

def main():
    mode = input("Choose mode: [1] CLI, [2] GUI: ").strip()
    if mode == "2" and gui_main:
        gui_main()
    else:
        play_game()

if __name__ == "__main__":
   main()  

  
