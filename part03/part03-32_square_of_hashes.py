def hash_square(length):
    i = 0
    while i < length:
        print("#" * length)
        i = i + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)
    print()
    hash_square(2)