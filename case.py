from os import unsetenv
import random
import collections
from typing import List

class Sukodu:

    def __init__(self, matrix):
        self.matrix = matrix

# ans = [     [5,3,4,6,7,8,9,1,2]
#             [6,7,2,1,9,5,3,4,8]
#             [1,9,8,3,4,2,5,6,7]
#             [8,5,9,7,6,1,4,2,3]
#             [4,2,6,8,5,3,7,9,1]
#             [7,1,3,9,2,4,8,5,6]
#             [9,6,1,5,3,7,2,8,4]
#             [2,8,7,4,1,9,6,3,5]
#             [3,4,5,2,8,6,1,7,9]
#              ]




    def validSudoku(self):

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for c in range(9):
            for r in range(9):
                if self.matrix[r][c] == 0:
                    continue
                if (self.matrix[r][c] in rows[r] or self.matrix[r][c] in cols[c] or self.matrix[r][c] in squares[r//3, c//3]):
                    return False

                cols[c].add(self.matrix[r][c])
                rows[r].add(self.matrix[r][c])
                squares[r//3, c//3].add(self.matrix[r][c])

        return True

    def spaceCount(self):
        size = 0
        for i in range(len(self.matrix)):           # row
            for j in range(len(self.matrix[i])):    # col
                if self.matrix[i][j] == 0:
                    #print(mat[i][j])
                    size +=1
                #sq[i][j] = question[i][j]
        return size

    def filled(self):
        nums = []
        zCnt  = 0
        space = self.spaceCount()
        fillcnt = 0
        if not self.validSudoku():
            return

        if space > 0:
            for i in range(len(self.matrix)):           # row
                for j in range(len(self.matrix[i])):    # col
                    if self.matrix[i][j] == 0:
                        nums = self.unusedNums(i, j)
                        if len(nums) > 0:
                            self.matrix[i][j] = nums[0]
##                            print("filled:", nums[0], "[", i+1, ",", j+1, "]")
                            fillcnt += 1
                            #print(i, j, nums[0])
                        else:
                            continue
                zCnt = self.countRow(j)
                if zCnt > 0:
                    print(i,j)
                    # swap
                    return

            for i in range(len(self.matrix)):
                print(self.matrix[i])

            print("-------", fillcnt)

            
            if fillcnt > 0:
                self.filled()

        return space


    def unusedNums(self, i, j):
        cellList = [1,2,3,4,5,6,7,8,9]
        t = l = 0   # top & left
        if (i // 3) == 0:
            t = 0
        elif (i //3) == 1:
            t = 3
        else:
            t = 6
        if (j // 3) == 0:
            l = 0
        elif (j //3) == 1:
            l = 3
        else:
            l = 6
        # remove used nums in 3x3 cells
        for x in range(t, t+3):
            for y in range(l, l+3):
                if self.matrix[x][y] != 0:
                    if self.matrix[x][y] in cellList:
                        cellList.remove(self.matrix[x][y])

        #remove used nums in row
        for y in range(len(self.matrix)):
            if self.matrix[i][y] != 0:
                if self.matrix[i][y] in cellList:
                    cellList.remove(self.matrix[i][y])

        #remove used nums in col
        for x in range(len(self.matrix)):
            #print(i,y, mat[i][y])
            if self.matrix[x][j] != 0:
                if self.matrix[x][j] in cellList:
                    cellList.remove(self.matrix[x][j])

        return cellList

    # def fillDiagonals(self):
    #     for r in range(9):
    #         for c in range(9):
    #             if (r - c) == 0 or (r + c) == 8:
    #                 if self.matrix[r][c] == 0: 
    #                     num = self.unusedNums(r,c)
    #                     if len(num) > 0:
    #                         self.matrix[r][c] = random.choice(num)   
    #                 else:
    #                     continue                     

    def fit(self, row: int):
        cntZero = 0
        cellList = []
        unRow = []
        cellListAddr = []
        r1 = 0
        c1 = 0

        for r in range(row):
            #cntZero = 0
            for c in range(9):
                if self.matrix[r][c] == 0: 
                    num = self.unusedNums(r,c)
                    if len(num) > 0:
                        self.matrix[r][c] = random.choice(num)   
            
            cntZero = self.countRow(r)

            #print(cntZero)
            if cntZero >= 0:
                unRow = self.unUsedInRow(r)
                cellList = self.unusedInRowGrid(r,c)
                if len(unRow) and len(cellList):
                    cellListAddr = self.cellListAddr(r, unRow[0], cellList)
                    print("len cell address", len(cellListAddr), cellListAddr)
                    #print(unRow[0], cellList, cellListAddr)
                    #self.matrix[r][c] = unRow[0]
                    if len(cellListAddr) > 0:
                        print(cellListAddr[0][0])
                        print(cellList)
                        print(unRow[0])
                        print(self.matrix[r][c])
                    # need checking
                        r1 = cellListAddr[0][1]
                        c1 = cellListAddr[0][2]
                        self.matrix[r][c] = unRow[0]
                        self.matrix[r1][c1], self.matrix[r][c] = self.matrix[r][c], self.matrix[r1][c1] 
                        # self.matrix[r][c], self.matrix[r1][c1] = self.matrix[r1][c1], self.matrix[r][c] 
                    else:
                        print("no address")
                    #self.matrix[r][c], self.matrix[cellListAddr[0][0]] = self.matrix[cellListAddr[0][0]],  self.matrix[r][c]
                    #print(cellListAddr)
            # #print(r, cntZero)
            # if cntZero > 0: 
            #     print("r", r, c, cntZero)
            #     unRow = self.unUsedInRow(r)
            #     cellList = self.unusedInRowGrid(r,c)
            #     print("unRow", unRow, cellList) 
            #     if unRow and cellList:
            #         #print("unRow", unRow)                    
            #         cellListAddr = self.cellListAddr(r, unRow[0], cellList)
            #         print(cellListAddr)
            #         # self.matrix[r][c] = num
            #         # self.matrix[r][c], cellListAddr[0][0] = cellListAddr[0][0], self.matrix[r][c]
            #     #print(l)
            #     print("after")
            #     for i in self.matrix:
            #         print(i)
            #     return
        # for i in range(len(self.matrix)):
        #     print(i)

    def countRow(self, row):
        zcnt = 0
        for r in range(row):
            for c in range(9):
                #print(r, c, self.matrix[row][c])
                if self.matrix[row][c] == 0:
                    zcnt += 1
        return zcnt



    def cellListAddr(self, row: int, num: int, cellList: List, ) -> dict:
        
        l = len(cellList)
        cellAddr = []   
        n = 0
        for c in range(9):
            if self.matrix[row][c] in cellList:
                cellAddr.append([self.matrix[row][c], row,c])
                n += 1
        #print("cellListAddr", cellAddr)
        return cellAddr

    def unUsedInRow(self, row: int) -> List:
        num = [1,2,3,4,5,6,7,8,9]
        for c in range(9):
            if self.matrix[row][c] in num:
                num.remove(self.matrix[row][c])
        return num

    # try to fit unused in in celllist[0] to celllist[-1]
    # check 3 x 3 valid: if yes, fit it
    # 
    #
    #



    def unusedInRowGrid(self, i, j):
        rowList = [1,2,3,4,5,6,7,8,9]
        cellList  = [1,2,3,4,5,6,7,8,9]
        t = l = 0   # top & left
        if (i // 3) == 0:
            t = 0
        elif (i //3) == 1:
            t = 3
        else:
            t = 6
        if (j // 3) == 0:
            l = 0
        elif (j //3) == 1:
            l = 3
        else:
            l = 6
        # for r in range(9):
        #     for c in range(9):
        #         if self.matrix[r][c] != 0:
        #             cellList.remove(self.matrix[r][c])
        for x in range(t, t+3):
            for y in range(l, l+3):
                if self.matrix[x][y] != 0:
                    if self.matrix[x][y] in cellList:
                        cellList.remove(self.matrix[x][y])
        

        
        #print("cellList", cellList)
        return cellList

        # # remove used nums in 3x3 cells
        # for x in range(t, t+3):
        #     for y in range(l, l+3):
        #         if self.matrix[x][y] != 0:
        #             if self.matrix[x][y] in cellList:
        #                 cellList.remove(self.matrix[x][y])

        # #remove used nums in row
        # for y in range(len(self.matrix)):
        #     if self.matrix[i][y] != 0:
        #         if self.matrix[i][y] in cellList:
        #             cellList.remove(self.matrix[i][y])







    def genSudoku(self):
        num1 = [1,2,3,4,5,6,7,8,9]
        # self.fillDiagonals()
        self.fit(6)
        #self.filled()
        print("\n")
        for i in range(9):
            print(self.matrix[i])

        print("space:", self.spaceCount())
        # num2 = num1.copy()
        # num3 = num1.copy()
        # num4 = num1.copy()
        # #small = [[0] * 3 for _ in range(3)]


        # for c in range(3):
        #     for r in range(3):
        #         temp = random.choice(num1)
        #         self.matrix[r][c] = temp
        #         num1.remove(temp)

        # for c in range(3,6):
        #     for r in range(3,6):
        #         temp = random.choice(num2)
        #         self.matrix[r][c] = temp
        #         num2.remove(temp)
        
        # for c in range(6,9):
        #     for r in range(6,9):
        #         temp = random.choice(num3)
        #         self.matrix[r][c] = temp
        #         num3.remove(temp)

        # for c in range(6,9):
        #     for r in range(3):
        #         temp = self.unusedNums(r,c)
        #         if len(temp) > 0:
        #             n = random.choice(temp)
        #             self.matrix[r][c] = n
        #         else:
        #             continue
        #         #num4.remove(temp)    

        # for c in range(3):
        #     for r in range(6,9):
        #         temp = self.unusedNums(r,c)
        #         if len(temp) > 0:
        #             n = random.choice(temp)
        #             self.matrix[r][c] = n
        #         else:
        #             continue

        # for c in range(3,6):
        #     for r in range(3):
        #         temp = self.unusedNums(r,c)
        #         if len(temp) > 0:
        #             n = random.choice(temp)
        #             self.matrix[r][c] = n
        #         else:
        #             continue

        # for c in range(3,6):
        #     for r in range(6,9):
        #         temp = self.unusedNums(r,c)
        #         if len(temp) > 0:
        #             n = random.choice(temp)
        #             self.matrix[r][c] = n
        #         else:
        #             continue

        # self.filled()            
        # for i in self.matrix:
        #     print(i , ",") 


        # t = l = 0   # top & left
        # if (i // 3) == 0:
        #     t = 0
        # elif (i //3) == 1:
        #     t = 3
        # else:
        #     t = 6
        # if (j // 3) == 0:
        #     l = 0
        # elif (j //3) == 1:
        #     l = 3
        # else:
        #     l = 6




        # # try 10 times to gen valid sudoku puzzle
        # #k = self.matrix.copy()

        # for i in range(10):
        #     self.matrix = [[0] * 9 for _ in range(9)]
        #     print ("gen", i)
        #     pick = random.randint(30,35)
        #     val = 0
        #     bolIsValid = False
        #     while (pick > 0):
        #         r = random.randint(0,8)
        #         c = random.randint(0,8)
        #         if self.matrix[r][c] == 0:
        #             num = self.unusedNums(r,c)
        #             val = random.choice(num)
        #             #print(num, val)
        #             self.matrix[r][c] = val
        #             if self.validSudoku() == False:
        #                 self.matrix[r][c] = 0
        #             else:
        #                 print(r, c, self.matrix[r][c])
        #                 pick -= 1
        #         else:
        #             continue
            
        #     if self.filled() > 0:
        #         #return self.matrix
        #         print (i, "Invalid matrix, redo.")
                
        #     else:
        #         print (i, "VALID")
        #         return self.matrix 
                
        # for i in range(9):
        #     print (self.matrix[i])

def action(n):
    # Generate new sudoku matrix
    print(1)
    if n == 0:            
        matrix = [[0] * 9 for _ in range(9)]
        for i in range(9):
            print (matrix[i])

        print("*************")
        game = Sukodu(matrix)
        game.genSudoku()

    # Find solution of sudoku
    elif n == 1:        
            # matrix = [  [5,3,0,0,7,0,0,0,0],
            #             [6,0,0,1,9,5,0,0,0],
            #             [0,9,8,0,0,0,0,6,0],
            #             [8,0,0,0,6,0,0,0,3],
            #             [4,0,0,8,0,3,0,0,1],
            #             [7,0,0,0,2,0,0,0,6],
            #             [0,6,0,0,0,0,2,8,0],
            #             [0,0,0,4,1,9,0,0,5],
            #             [0,0,0,0,8,0,0,7,9]
            #             ]

            matrix = [  
                        [2, 5, 1, 0, 0, 0, 9, 7, 8],
                        [8, 7, 6, 0, 0, 0, 5, 4, 0],
                        [3, 4, 9, 0, 0, 0, 6, 1, 0],
                        [0, 0, 0, 5, 3, 8, 0, 0, 0],
                        [0, 0, 0, 7, 1, 9, 0, 0, 0],
                        [0, 0, 0, 6, 2, 4, 0, 0, 0],
                        [5, 2, 8, 0, 0, 0, 7, 6, 3],
                        [7, 1, 0, 0, 0, 0, 4, 9, 5],
                        [9, 3, 4, 0, 0, 0, 1, 8, 2],
                    ]


            game = Sukodu(matrix)
            game.filled()



if __name__ == "__main__":

    action(0)


