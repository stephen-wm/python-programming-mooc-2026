list = []

while True:
    value = input("Word: ")

    if value in list:
        break
    else:
        list.append(value)

print(f"You typed in {len(list)} different words")