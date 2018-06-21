__author__ = 'Andrei'


class MkBlank:
    def __init__(self, file):
        self.file = file

    def generate_blank(self):
        f = open(self.file, 'w')
        try:
            for i in range(1, 10):
                for j in range(1, 10):
                    if j < 9:
                        temp = str(i) + str(j) + '=0, '
                    else:
                        temp = str(i) + str(j) + '=0 '
                    f.write("%s" % temp)
                    print(temp, end='')
                f.write("%s" % '\n')
                print()
        finally:
            f.close()


def main():
    directory = "C:/Users/andrei/Documents/data/sudoku/"
    file_name = "sudoku_puzzle.txt"
    mb = MkBlank(directory + file_name)
    mb.generate_blank()


if __name__ == "__main__":
    main()
