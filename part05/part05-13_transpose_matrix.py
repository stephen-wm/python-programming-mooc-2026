def transpose(matrix: list):
    size = len(matrix)

    for row in range(size):
        for col in range(row + 1, size):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
