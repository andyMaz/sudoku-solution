from sudoku.solve import Solve

__author__ = 'Andrei'


class Assist(object):
    def __init__(self, b, out):
        self.puzzle = b.get_puzzle()
        self.solve = Solve(b, out)
        self.out = out

    def help(self):
        f = open(self.out, 'w')
        print()
        try:
            f.write('\n\n')
            for i in range(9):
                for j in range(9):
                    if self.puzzle[i][j] == 0:
                        f.write("%9s" % self.print_lst(self.solve.possibilities(i, j)) + " ")
                        print("%9s" % self.print_lst(self.solve.possibilities(i, j)) + " ", end='')
                    else:
                        f.write("%9s" % str(self.puzzle[i][j]) + " ")
                        print("%9s" % str(self.puzzle[i][j]) + " ", end='')
                    if j % 3 == 2 and j != 8:
                        f.write(" |  ")
                        print(" |  ", end='')
                f.write('\n')
                print()
                if i % 3 == 2 and i != 8:
                    f.write('\t' + ('-' * 95) + '\n')
                    print('\t' + ('-' * 95))
        finally:
            f.close()

    @staticmethod
    def print_lst(ls):
        temp = ''
        for l in ls:
            temp += str(l)
        return temp
