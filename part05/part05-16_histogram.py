def histogram(my_string: str):
    letters = {}
    
    for char in my_string:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    
    for letter in letters:
        print(f"{letter} {'*' * letters[letter]}")
