
from sudoku.gui import SudokuGUI
from tkinter import *

__author__ = 'Andrei'


def main():
    directory = "io/"
    root = Tk()
    root.title("  Sudoku")
    root.resizable(width=False, height=False)
    root.wm_iconbitmap('image/sudoku.ico')
    _ = SudokuGUI(root, directory, "sudoku_puzzle.txt")

    root.mainloop()


if __name__ == "__main__":
    main()
