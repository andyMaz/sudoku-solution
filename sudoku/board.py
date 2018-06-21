import csv

__author__ = 'Andrei'


class Puzzle(object):
    def __init__(self, in_file):
        self.in_file = in_file
        self.puzzle = [[0 for _ in range(9)] for _ in range(9)]

    def get_puzzle(self):
        return self.puzzle

    def __str__(self):
        temp = ''
        for i in range(9):
            for j in range(9):
                temp += str(self.puzzle[i][j]) + ' '
                if j % 3 == 2:
                    temp += '\t'
            temp += '\n'
            if i % 3 == 2:
                temp += '\n'
        return temp

    def read_puzzle(self):
        f = open(self.in_file, 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                for e in row:
                    cs = e.split('=')
                    c = int(cs[0].strip())
                    if cs[1].strip() == '':
                        v = int('0')
                    else:
                        v = int(cs[1].strip())
                    x = c // 10
                    y = c - (x * 10)
                    self.puzzle[x - 1][y - 1] = v
                # print()
        finally:
            f.close()

    @staticmethod
    def index(n):
        r = n // 9
        c = n % 9
        return r, c
