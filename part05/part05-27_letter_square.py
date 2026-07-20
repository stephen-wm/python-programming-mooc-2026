layers = int(input("Layers: "))
size = layers * 2 - 1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for row in range(size):
    for col in range(size):
        top = row
        left = col
        bottom = size - row - 1
        right = size - col - 1
        distance = min(top, left, bottom, right)

        print(letters[layers - distance - 1], end="")
    print()
