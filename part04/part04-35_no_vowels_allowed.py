def no_vowels(my_string: str):
    for vowel in "aeiou":
        my_string = my_string.replace(vowel, "")

    return my_string
    

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
