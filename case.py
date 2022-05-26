

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

import collections
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

def validSudo(mat):

    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for c in range(9):
        for r in range(9):
            if mat[r][c] == 0:
                continue
            if (mat[r][c] in rows[r] or mat[r][c] in cols[c] or mat[r][c] in squares[r//3, c//3]):
                return False

            cols[c].add(mat[r][c])
            rows[r].add(mat[r][c])
            squares[r//3, c//3].add(mat[r][c])

    return True


def spaceCount(mat):
    size = 0;
    for i in range(len(mat)):           # row
        for j in range(len(mat[i])):    # col
            if mat[i][j] == 0:
                #print(mat[i][j])
                size +=1
            #sq[i][j] = question[i][j]
    return size

def filled(mat):
    nums = []
    space = spaceCount(mat)

    if not validSudo(mat):
        return

    if space > 0:
        for i in range(len(mat)):           # row
            for j in range(len(mat[i])):    # col
                if mat[i][j] == 0:
                    nums = unusedNums(mat, i, j)
                    if len(nums) == 1:
                        mat[i][j] = nums[0]
                        #print(i, j, nums[0])
                    else:
                        continue

        for i in range(len(mat)):
            print(mat[i])

        print("-------")
        filled(mat)


def unusedNums(mat, i, j):
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
            if mat[x][y] != 0:
                if mat[x][y] in cellList:
                    cellList.remove(mat[x][y])

    #remove used nums in row
    for y in range(len(mat)):
        if mat[i][y] != 0:
             if mat[i][y] in cellList:
                 cellList.remove(mat[i][y])

    #remove used nums in col
    for x in range(len(mat)):
        #print(i,y, mat[i][y])
        if mat[x][j] != 0:
             if mat[x][j] in cellList:
                 cellList.remove(mat[x][j])
    return cellList



num = [1,2,3,4,5,6,7,8,9]

n = spaceCount(matrix)
#print(n)

r = 0
c = 4
unusedNums(matrix, r, c)
filled(matrix)
