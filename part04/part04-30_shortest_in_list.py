def shortest(my_list: list):
    short = my_list[0]
    
    for item in my_list:
        if len(item) < len(short):
            short = item
 
    return short
 
if __name__ == "__main__":
    a = ["first", "second", "fourth", "eleventh"]
    result1 = shortest(a)
    print(result1)
 
    b = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
 
    result2 = shortest(b)
    print(result2)