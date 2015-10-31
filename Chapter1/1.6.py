def rotate_90(matrix):
    n = len(matrix)
    new_matrix = []
    for _ in range(n):
        new_matrix.append([0]*n)
    
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-i-1] = matrix[i][j]
    return new_matrix

mat = rotate_90([ [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9] ])

for row in mat:
    print(row)
