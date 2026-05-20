def length_of_longest(my_list: list):
    longest = 0
    for item in my_list:
        if len(item) > longest:
            longest = len(item)
 
    return longest
 
if __name__ == "__main__":
    a = ["first", "second", "fourth", "eleventh"]
    result1 = length_of_longest(a)
    print(result1)
 
    b = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
 
    result2 = length_of_longest(b)
    print(result2)