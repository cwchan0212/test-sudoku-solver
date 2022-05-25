

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

def numOfSpace(mat):
    space = 0;
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                #print(mat[i][j])
                space +=1
            #sq[i][j] = question[i][j]
    return space

# rows = collections.defaultdict(set)
# cols = collections.defaultdict(set)
# squares = collections.defaultdict(set)

num = [1,2,3,4,5,6,7,8,9]

n = numOfSpace(matrix)
print(n)



# def validSudo:
#     for c in range(9):
#         for r in range(9):
#             if matrix[r][c] == 0:
#                 continue
#             if (matrix[r][c] in rows[r] or matrix[r][c] in cols[c] or matrix[r][c] in squares[r//3, c//3]):
#                 return False

#             cols[c].add(matrix[r][c])
#             rows[r].add(matrix[r][c])
#             squares[r//3, c//3].add(matrix[r][c])
#     return True
