def line(length, string):
    if string != "":
        print(string[0] * length)
    else:
        print("*" * length)
 
def triangle(size):
    # You should call function line here with proper parameters
    index = 1
    while index <= size:
        line(index, "#")
        index = index + 1
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)