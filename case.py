import collections

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

    def validSudo(self):

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


    def spaceCount(self, mat):
        size = 0;
        for i in range(len(mat)):           # row
            for j in range(len(mat[i])):    # col
                if mat[i][j] == 0:
                    #print(mat[i][j])
                    size +=1
                #sq[i][j] = question[i][j]
        return size

    def filled(self):
        nums = []
        space = self.spaceCount(self.matrix)

        if not self.validSudo():
            return

        if space > 0:
            for i in range(len(self.matrix)):           # row
                for j in range(len(self.matrix[i])):    # col
                    if self.matrix[i][j] == 0:
                        nums = self.unusedNums(i, j)
                        if len(nums) == 1:
                            self.matrix[i][j] = nums[0]
                            #print(i, j, nums[0])
                        else:
                            continue

            for i in range(len(self.matrix)):
                print(self.matrix[i])

            print("-------")
            self.filled()


    def unusedNums(self, i, j):
        cellList = [1,2,3,4,5,6,7,8,9]
        t = l = 0
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

if __name__ == "__main__":

    matrix = [  [5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]
                ]
    
    game = Sukodu(matrix)

    num = [1,2,3,4,5,6,7,8,9]

    n = game.spaceCount(matrix)
    print(n)

    r = 0
    c = 4
    game.unusedNums(r, c)
    game.filled()
