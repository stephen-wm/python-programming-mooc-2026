def print_sudoku(sudoku: list):
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                print("_", end=" ")
            else:
                print(sudoku[row][col], end=" ")

            if col % 3 == 2 and col != 8:
                print(" ", end="")
        
        print()

        if row % 3 == 2 and row != 8:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    cloned = []
    for sublist in sudoku:
        cloned.append(sublist[:])
    add_number(cloned, row_no, column_no, number)
    return cloned

# def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#     cloned = []
#     for sublist in sudoku:
#         cloned.append(sublist[:])
#     cloned[row_no][column_no] = number
#     return cloned

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)