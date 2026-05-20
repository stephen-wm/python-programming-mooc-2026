def anagrams(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    elif sorted(s1.lower()) != sorted(s2.lower()):
        return False
    
    return True
 
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False