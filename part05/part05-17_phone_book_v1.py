phonebook = {}

while True:
    option = input("command (1 search, 2 add, 3 quit): ")
    if option == "3":
        print("quitting...")
        break
    if option == "1":
        name = input("name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("no number")
    if option == "2":
        name = input("name: ")
        number = input("number: ")
        phonebook[name] = number
        print("ok!")
