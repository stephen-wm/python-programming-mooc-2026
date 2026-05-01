def squared(string, times):
    index = 0
    i = 0

    while i < times:
        row = ""
        j = 0

        while j < times:
            if index == len(string):
                index = 0
            row = row + string[index]
            index = index + 1
            j = j + 1
        print(row)
        i = i + 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
