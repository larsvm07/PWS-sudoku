import random
sudoku = [
    [0, 3, 4, 0],
    [4, 0, 0, 2],
    [1, 0, 0, 3],
    [0, 2, 1, 0]
]
matrix_solved = [
    [2, 3, 4, 1],
    [4, 1, 3, 2],
    [1, 4, 2, 3],
    [3, 2, 1, 4]
]
matrix_copy = [row[:] for row in sudoku]


def check(checkmatrix):
    global solved
    solved = True
    for row in range(4):  # checks rows
        if [1, 2, 3, 4] != sorted(checkmatrix[row]):
            solved = False
            break
    if solved:
        for col in range(4):
            column = [checkmatrix[row][col] for row in range(4)]
            if sorted(column) != [1, 2, 3, 4]:
                solved = False
                break
    if solved:
        blocks = [
            [matrix_solved[0][0], matrix_solved[0][1],
                matrix_solved[1][0], matrix_solved[1][1]],
            [matrix_solved[0][2], matrix_solved[0][3],
                matrix_solved[1][2], matrix_solved[1][3]],
            [matrix_solved[2][0], matrix_solved[2][1],
                matrix_solved[3][0], matrix_solved[3][1]],
            [matrix_solved[2][2], matrix_solved[2][3],
                matrix_solved[3][2], matrix_solved[3][3]]
        ]
        for i in range(4):
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