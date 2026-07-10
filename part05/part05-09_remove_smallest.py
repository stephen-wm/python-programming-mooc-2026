def remove_smallest(my_list: list):
    smallest = my_list[0]
    for item in my_list:
        if item < smallest:
            smallest = item
    
    my_list.remove(smallest)
    
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)