def palindromes(string: str):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True
 
while True:
    string = input("Please type in a palindrome: ")
    if palindromes(string) == False:
        print("that wasn't a palindrome")
    else:
        print(f"{string} is a palindrome!")
        break
 