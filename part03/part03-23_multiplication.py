limit = int(input("Please type in a number: "))
i = 1

while i <= limit:
    j = 1
    while j <= limit:
        print(f"{i} x {j} = {i * j}")
        j = j + 1
    i = i + 1