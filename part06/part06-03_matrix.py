def read_matrix() -> list:
    matrix = []

    with open("matrix.txt") as file:
        for line in file:
            row = []

            for number in line.split(','):
                row.append(int(number))

            matrix.append(row)
            
    return matrix

def matrix_sum() -> int:
    sum = 0

    for row in read_matrix():
        for number in row:
            sum += number
    
    return sum

def matrix_max() -> int:
    largest = 0

    for row in read_matrix():
        for number in row:
            if number > largest:
                largest = number
    
    return largest

def row_sums() -> list:
    sums = []

    for row in read_matrix():
        total = 0

        for number in row:
            total += number

        sums.append(total)

    return sums