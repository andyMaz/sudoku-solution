from sudoku.board import Puzzle


__author__ = 'Andrei'


class Solve(object):
    def __init__(self, b, out):
        self.board = b
        self.puzzle = b.puzzle
        self.file = out

    def row(self, i):
        """
        :param i: for any row i
        :return: all elements that are not in row i
        """
        s = []
        for j in range(9):
            if not (self.puzzle[i][j] == 0):
                s.append(self.puzzle[i][j])
        return s

    def column(self, j):
        """
        :param j: for any column j
        :return: returns all elements that are not in column j
        """
        s = []
        for i in range(9):
            if not (self.puzzle[i][j] == 0):
                s.append(self.puzzle[i][j])
        return s

    def box(self, i, j):
        """
        :param i:  row index
        :param j:  column index
        :return: for cell (i, j) return list of numbers that are not in the same box
        """
        si = self.find_box_start(i)
        sj = self.find_box_start(j)
        s = []
        for p in range(si, si + 3):
            for q in range(sj, sj + 3):
                if not (self.puzzle[p][q] == 0):
                    s.append(self.puzzle[p][q])
        return s

    @staticmethod
    def find_box_start(n):
        """
        :param n:  value of any row/column
        :return:   value of starting row/column of the box n belongs to
        """
        return 3 * (n//3)

    def possibilities(self, i, j):
        """
        :param i: row index
        :param j: column index
        :return: for cell (i, j) it returns, list of potential possible values given numbers already on the board
        """
        s = []
        if self.puzzle[i][j] == 0:
            s.extend(self.row(i))
            s.extend(self.column(j))
            s.extend(self.box(i, j))
        return [p for p in range(1, 10) if p not in s]

    def to_file(self):
        for i in range(9):
            for j in range(9):
                self.file.write(str(self.puzzle[i][j]) + ' ')
                if j % 3 == 2:
                    self.file.write('\t')
            self.file.write('\n')
            if i % 3 == 2:
                self.file.write('\n')

    def sudoku(self, n):
        """
        A backtracking method that solves a sudoku puzzle

        :param n: next position to consider filling
        :return:
        """
        if n < 81:
            r, c = Puzzle.index(n)
            if self.puzzle[r][c] == 0:
                ps = self.possibilities(r, c)
                for x in ps:
                    self.puzzle[r][c] = x  # tentative placing of value x at position n
                    self.sudoku(n + 1)
                    # checking if the board is full
                    if n+1 == 81:
                        print(self.board)
                        self.to_file()
                    self.puzzle[r][c] = 0  # backtracking
            else:
                # checking if the board is full
                if n+1 == 81:
                    print(self.board)
                    self.to_file()
                self.sudoku(n + 1)
