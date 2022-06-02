from os import unsetenv
import random
import collections

class Sudoku:

    # matrix = []
    # n = 0   # no. of columns / rows
    # sqn = 0 # square root of n
    # k = 0   # no. of missing digits

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.sqn = math.sqrt(n)
        self.mat = [n][n]

    def fillBox(row, col):
        num = 0;
        for i in range(len(sqn)):
            for j in range(len(sqn)):
                num = randomGenerator()
                while (unUsedInBox(top, left, num) == True):
                    mat[row+i][col+j] = num

    def randomGenerator(self) -> int:
        no = [1,2,3,4,5,6,7,8,9]
        return random.choice(no)

    def unUsedInBox(self, top, left, num) -> bool:
        for i in range(self.sqn):
            for j in range(self.sqn):
                if (mat[top+i][left+i] == num):
                    return False
        return True
