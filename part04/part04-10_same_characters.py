def same_chars(string, a, b):
    if a < 0 or b < 0:
        return False
 
    if a >= len(string) or b >= len(string):
        return False
    
    return string[a] == string[b]
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 6, 7)) # True
 
    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False
 
    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False