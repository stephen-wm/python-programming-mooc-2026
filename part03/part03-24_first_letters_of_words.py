string = input("Please type in a sentence: ")
i = 0

while i < len(string):
    print(string[i])
    
    while i < len(string) and string[i] != ' ':
        i = i + 1
    
    while i < len(string) and string[i] == ' ':
        i = i + 1