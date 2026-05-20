def all_the_longest(my_list: list):
    longest = 0
    new_list = []
    
    for item in my_list:
        if len(item) > longest:
            longest = len(item)
 
    for item in my_list:
        if len(item) == longest:
            new_list.append(item)
 
    return new_list
 
if __name__ == "__main__":
    a = ["first", "second", "fourth", "eleventh"]
    result1 = all_the_longest(a)
    print(result1)
 
    b = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
 
    result2 = all_the_longest(b)
    print(result2)