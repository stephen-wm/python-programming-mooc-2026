def line(length, string):
    if string != "":
        print(string[0] * length)
    else:
        print("*" * length)
 
def shape(width, character, height, symbol):
    i = 1
    while i <= width:
        line(i, character)
        i = i + 1 
    
    # You want to print height number of rows, each with length width.
    j = 1
    while j <= height:
        # Pass width as the argument for line not height or any other variable
        line(width, symbol)
        j += 1
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")