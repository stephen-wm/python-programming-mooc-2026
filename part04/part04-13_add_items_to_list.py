list = []
items = int(input("How many times: "))
index = 1

while index <= items:
    value = int(input(f"Item {index}: "))
    list.append(value)

    index = index + 1

print(list)