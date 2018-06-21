from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from sudoku.board import Puzzle
from sudoku.assistance import Assist
from sudoku.solve import Solve

__author__ = 'Andrei'


class SudokuGUI:
    def __init__(self, master, dr, pt):
        self.dir = dr
        self.input = pt
        self.master = master
        self.puzzle = [[StringVar() for _ in range(9)] for _ in range(9)]
        self.top_frame = Frame(master, height=2, bd=2, relief=RIDGE)
        self.top_frame.grid(row=0, column=0)
        self.frame = [[Frame(self.top_frame, height=2, bd=2, relief=RIDGE) for _ in range(3)] for _ in range(3)]
        self.count = 0
        n = 0
        for r in range(3):
            for c in range(3):
                self.box(self.frame[r][c], n).grid(row=r, column=c)
                n += 1

        self.bottom_frame = Frame(master)
        self.bottom_frame.grid(row=1, column=0)
        self.save_button = ttk.Button(self.bottom_frame, text="Save", command=self.save_sudoku, state=DISABLED)
        self.save_button.grid(row=0, column=0)
        self.open_button = ttk.Button(self.bottom_frame, text="Open", command=self.open_sudoku)
        self.open_button.grid(row=0, column=1)

        self.solve_button = ttk.Button(self.bottom_frame, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=0, column=2)

        ttk.Button(self.bottom_frame, text="Exit", command=self.exit_sudoku).grid(row=0, column=3)
        for r in range(9):
            for c in range(9):
                self.puzzle[r][c].trace("w", lambda name, index,
                                        mode, sv=self.puzzle[r][c]: self.callback())

    def solve_sudoku(self):
        filename = filedialog.askopenfile(initialdir=self.dir,
                                          filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                          title="Choose a file.")

        self.open_button.state(["disabled"])
        print(filename.name)
        b = Puzzle(filename.name)
        b.read_puzzle()
        print(b)

        a = Assist(b, self.dir + "sudoku_help.txt")
        a.help()
        print()
        out = open(self.dir + "solution.txt", 'w')
        try:
            sl = Solve(b, out)
            sl.sudoku(0)
        finally:
            out.close()

    def callback(self):
        self.save_button.config(state="normal")

    def box(self, master, n):
        entry = []
        for r in range(3):
            q = []
            for c in range(3):
                e = Entry(master, width=5, font="Helvetica 10 bold", textvariable=self.puzzle[n][(3 * r) + c],
                          justify='center')
                if n % 2 == 0:
                    e.config(background='cyan')
                q.append(e)
            entry.append(q)

        for r in range(3):
            for c in range(3):
                entry[r][c].grid(row=r, column=c)
                self.puzzle[n][(3 * r) + c].set(0)
        return master

    def save_sudoku(self):
        self.save_button.state(["disabled"])
        self.open_button.state(["disabled"])
        b = Puzzle(self.dir + self.input)
        b.read_puzzle()
        p = self.transform()
        self.print_sudoku(p)
        print()
        self.write_puzzle(p)

    def open_sudoku(self):
        filename = filedialog.askopenfile(initialdir=self.dir,
                                          filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                          title="Choose a file")

        self.open_button.state(["disabled"])
        print(filename.name)
        b = Puzzle(filename.name)

        b.read_puzzle()
        print(b)
        self.trans_bk(b.puzzle)

    def trans_bk(self, p):
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                self.to_box(r, c, p)

    def to_box(self, x, y, p):
        for r in range(x, x + 3):
            for c in range(y, y + 3):
                i, j = Puzzle.index(self.count)
                self.puzzle[r][c].set(p[i][j])
                self.count += 1

    def exit_sudoku(self):
        self.master.destroy()

    def back_to_bord(self, b):
        for r in range(9):
            for c in range(9):
                self.puzzle[r][c].set(b[r][c])

    def transform(self):
        p = []
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                q = []
                for r in range(x, x + 3):
                    for c in range(y, y + 3):
                        q.append(self.puzzle[r][c].get())
                p.append(q)
        return p

    @staticmethod
    def print_sudoku(p):
        for r in range(9):
            for c in range(9):
                print("%3s" % p[r][c] + ' ', end='')
                if c % 3 == 2:
                    print('  ', end='')
            print()
            if r % 3 == 2:
                print()

    @staticmethod
    def comma_sep(ls):
        temp = ''
        for e in ls[:-1]:
            temp += e + ', '
        if ls:
            temp += ls[len(ls) - 1]
        return temp

    def write_puzzle(self, p):
        f = open(self.dir + self.input, 'w')
        try:
            for r in range(9):
                tmp = []
                for c in range(9):
                    tmp.append(str(r + 1) + str(c + 1) + '=' + p[r][c])
                    cs = self.comma_sep(tmp)
                if cs != '':
                    print(cs)
                    f.write(cs)
                    f.write('\n')
                if r % 3 == 2:
                    print()
                    f.write('\n')
        finally:
            f.close()


def main():
    directory = "io/"

    root = Tk()
    root.title("Sudoku")
    _ = SudokuGUI(root, directory, "sudoku_puzzle.txt")
    root.mainloop()


if __name__ == "__main__":
    main()
