limit = int(input("Please type in a number: "))
left = 1
right = limit

while left <= right:
    print(left)

    if left != right:
        print(right)

    left = left + 1
    right = right - 1
