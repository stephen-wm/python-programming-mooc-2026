def line(length, string):
    if string != "":
        print(string[0] * length)
    else:
        print("*" * length)
 
def square_of_hashes(size):
    # You should call function line here with proper parameters
    index = 0
    while index < size:
        line(size, "#")
        index = index + 1
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)