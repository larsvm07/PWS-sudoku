
l_nums_x = [8, 3, 0, 5, 0, 0, 0, 9, 0] 
t_nums_x = (8, 3, 0, 5, 0, 0, 0, 9, 0)

l_nums_y = [0,1,2,3,4,5,6,7,8]
t_nums_y = (0,1,2,3,4,5,6,7,8)

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

matrix_y = [
    
]

for row in range(len(matrix)):
    for i in range(len(matrix[row])):
        column = matrix[row][i]
        matrix_y.append(column)
print(matrix_y)
    

def solve(l_row, t_row, l_column, t_column):
    uniques = []
    for item in range(len(t_row)):      # voor elke waarde in t_row
        if t_row[item] != 0:
            unique = t_row[item]
            uniques.append(unique)      # alle waarden uit tuple (=de sudoku) toevoegen aan uniques
    
    for item in range(len(l_row)):
        value = l_row[item]
        if value in t_row and uniques:
            value = 1
        while value in uniques:
            value += 1
            
        if value not in uniques:
            uniques.append(value)
            l_row[item] = value    
    return l_row 
    

def solve2(l_row, t_row, l_column, t_column):
    for item in range(len(t_row)):
        unavailable = []
        if t_row[item] != 0:
            unavailable.append(t_row[item])
        for item in range(len(t_column)):
            if t_column[item] != 0 and t_column[item] not in unavailable:
                unavailable.append(t_column[item])
    return unavailable 

print(solve(l_nums_x, t_nums_x, l_nums_y, t_nums_y))