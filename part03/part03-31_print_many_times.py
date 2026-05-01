def print_many_times(text, times):
    i = 0

    while i < times:
        print(text)
        i = i + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
    print_many_times("All Pythons, except one, grow up", 3)