def add_person(phonebook: dict):
    name = input("name: ")
    number = input("number: ")
    if name in phonebook:
        phonebook[name].append(number)
    else:
        phonebook[name] = [number]
    print("ok!")

def lookup(phonebook: dict):
    name = input("name: ")
    if name in phonebook:
        for number in phonebook[name]:
            print(number)
    else:
        print("no number")

phonebook = {}

while True:
    option = input("command (1 search, 2 add, 3 quit): ")

    if option == "3":
        print("quitting...")
        break
    if option == "1":
        lookup(phonebook)
    if option == "2":
        add_person(phonebook)
