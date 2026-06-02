# def most_common_character(my_string: str):
#     best_char = my_string[0]
#     best_count = 0

#     for char in my_string:
#         current_count = 0

#         for next_char in my_string:
#             if char == next_char:
#                 current_count = current_count + 1

#         if current_count > best_count:
#             best_count = current_count
#             best_char = char

#     return best_char      

def most_common_character(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character

    return most_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))