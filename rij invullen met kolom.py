
matrix = [
    [5, 0, 0,   0, 8, 0,   0, 4, 9],
    [0, 0, 0,   5, 0, 0,   0, 3, 0],
    [0, 6, 7,   3, 0, 0,   0, 0, 1],

    [1, 5, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   2, 0, 8,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 1, 8],
    
    [7, 0, 0,   0, 0, 4,   1, 5, 0],
    [0, 3, 0,   0, 0, 2,   0, 0, 0],
    [4, 9, 0,   0, 5, 0,   0, 0, 3]
]


t_matrix = (
    [5, 0, 0, 0, 8, 0, 0, 4, 9],
    [0, 0, 0, 5, 0, 0, 0, 3, 0],
    [0, 6, 7, 3, 0, 0, 0, 0, 1],
    
    [1, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 8],
    
    [7, 0, 0, 0, 0, 4, 1, 5, 0],
    [0, 3, 0, 0, 0, 2, 0, 0, 0],
    [4, 9, 0, 0, 5, 0, 0, 0, 3]
)
blocks = [

]
matrix_y = [
    
]

#for i in range(len(matrix)):
#    matrix_y.append([row[i] for row in matrix])
#print(matrix_y)

""""def blokken_bouwen(sudoku):
    # itereert over iedere rij in sudoku
    for row in sudoku:
        blocks.append(row[0:3])
    for row in sudoku:
        blocks[row].append(3:6)"""
block1 = matrix[0][0:3] + matrix[1][0:3] + matrix[3][0:3]


print(block)
#blokken_bouwen(matrix)  
#print(blocks)



