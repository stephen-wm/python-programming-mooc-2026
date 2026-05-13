list = []

while True:
    value = int(input("New item: "))

    if value == 0:
        break

    list.append(value)
    print("The list now:", list)
    print("The list in order:", sorted(list))

print("Bye!")