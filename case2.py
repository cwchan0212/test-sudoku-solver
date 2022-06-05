from os import unsetenv
from tkinter import N
from typing import List
import math
import random
import collections

class Sudoku:

    #matrix = []
    #n = 0   # no. of columns / rows
    #sqn = 0 # square root of n
    #k = 0   # no. of missing digits

    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        self.sqn = math.sqrt(n)
        self.mat = [n][n]

    def fillBox(row: int, col: int):
        num = 0;
        for i in range(len(self.sqn)):
            for j in range(len(self.sqn)):
                num = self.randomGenerator()
                while (self.unUsedInBox(top, left, num) == True):
                    mat[row+i][col+j] = num

    def fillDiagonal():
        for i in range(sqn):
            fillBox(i, i)

    def randomGenerator(self) -> int:
        no = [1,2,3,4,5,6,7,8,9]
        return random.choice(no)

    def unUsedInBox(self, top: int, left: int, num: int) -> bool:
        for i in range(self.sqn):
            for j in range(self.sqn):
                if (mat[top+i][left+i] == num):
                    return False
        return True

    def fillRemaining(self, i: int, j: int) -> bool:

        if j>=n and i<self.n-1:
            i = i+1
            j = 0

        if i>=n and j>=n:
            return True

        if i < self.sqn:
            if j < self.sqn:
                j = self.sqn
        elif i < self.n-self.sqn:
            if j == int(i/self.sqn*self.sqn):
                j = j + self.sqn
        else:
            if (j == self.n-self.sqn):
                i = i + 1
                j = 0
                if (i>=self.n):
                    return True

        for num in range(self.n):
            if (self.checkIfSafe(i, j, self.num)):
                self.mat[i][j] = num
                if (self.fillRemaining(i, j+1)):
                    return True
                self.nat[i][j] = 0
        return False

    def removeKDigits(self):
        count = self.k
        while (count != 0):
            cellID = self.randomGenerator(self.n * self.n)-1
            i = cellID / n
            j = cellID % 9
            if (j != 0):
                j -= 1
            if (self.mat[i][j] != 0):
                count -= 1
                self.mat[i][j] = 0
            
    def checkIfSafe(self, i: int, j: int, num: int) -> bool:
        return (unUsedInRow(i, num) and unUsedInCol(j, num) and unUsedInBox(i - i % self.sqn, i - i % self.sqn, num))

    def unUsedInRow(self, i: int, j: int, num: int) -> bool:
        for j in range(self.n):
            if self.matrix[i][j] == num:
                return False
        return True


# unUsedInCol
