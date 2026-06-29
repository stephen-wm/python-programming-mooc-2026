# First solution
# def longest(strings_list: list):
#     curr_longest = ""
#     curr_length = 0

#     for string in strings_list:
#         if len(string) > curr_length:
#             curr_length = len(string)
#             curr_longest = string

#     return curr_longest    

# if __name__ == "__main__":
#     strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
#     print(longest(strings))

# Final solution
def longest(strings_list: list):
    curr_longest = ""

    for string in strings_list:
        if len(string) > len(curr_longest):
            curr_longest = string

    return curr_longest    

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))