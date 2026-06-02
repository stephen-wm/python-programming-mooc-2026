def longest_series_of_neighbours(my_list: list):
    longest = 1
    current = 1

    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i - 1]) == 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))