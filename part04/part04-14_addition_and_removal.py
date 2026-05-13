list = []

while True:
    print("The list is now", list)
    
    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == "x":
        break
    elif action == "d":
        list.append(len(list) + 1)
    elif action == "r":
        # if list is empty don't remove anything
        if len(list) > 0:
            list.pop()
            # list.pop(len(list) - 1)
        else:
            continue

print("Bye!")