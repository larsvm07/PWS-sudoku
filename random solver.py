import random
sudoku = [
    [0, 0, 0, 0],
    [0, 3, 2, 0],
    [0, 4, 3, 0],
    [0, 1, 0, 0]
]









def check(checkmatrix):
    global solved
    solved = True
    for row in range(4):  # checks rows
        if [1, 2, 3, 4] != sorted(checkmatrix[row]):
            solved = False
            break
    if solved:
        for col in range(4): # checks colums
            column = [checkmatrix[row][col] for row in range(4)]
            if sorted(column) != [1, 2, 3, 4]:
                solved = False
                break
    if solved:
        blocks = [
            [checkmatrix[0][0], checkmatrix[0][1],
                checkmatrix[1][0], checkmatrix[1][1]],
            [checkmatrix[0][2], checkmatrix[0][3],
                checkmatrix[1][2], checkmatrix[1][3]],
            [checkmatrix[2][0], checkmatrix[2][1],
                checkmatrix[3][0], checkmatrix[3][1]],
            [checkmatrix[2][2], checkmatrix[2][3],
                checkmatrix[3][2], checkmatrix[3][3]]
        ]
        for i in range(4): # checks blocks (2x2)
            block = blocks[i]
            if sorted(block) != [1, 2, 3, 4]:
                solved = False
                break


def solve(matrix):
    matrix_copy = [row[:] for row in matrix]
    global solved
    solved = False
    while not solved:
        for row in range(4):
            for i in range(4):
                if matrix[row][i] == 0:
                    matrix_copy[row][i] = random.randint(1, 4)
        check(matrix_copy)
        print(matrix_copy)
    return matrix_copy


solved_matrix = solve(sudoku)
print(solved_matrix)

#het werkt nu eindelijk