my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))

    if index == -1:
        break

    if index < 0 or index >= len(my_list):
        print("Index is outside of the range of the list")
        continue

    value = int(input("Value: "))

    my_list[index] = value
    
    print(my_list)