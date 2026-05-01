def chessboard(size):
    i = 0
    while i < size:
        j = 0
        row = ""

        while j < size:
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
                
            j = j + 1
        print(row)
        i = i + 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
    chessboard(5)
    chessboard(6)
