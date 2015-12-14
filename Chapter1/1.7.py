def scan(matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[:])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_lines(i, j, new_matrix)
    return new_matrix

def zero_lines(i, j, matrix):
    for x in range(len(matrix[i])):
        matrix[i][x] = 0
    for y in range(len(matrix)):
        matrix[y][j] = 0

print(scan( [ [1, 1, 1],
              [0, 1, 1],
              [1, 1, 1] ]))
