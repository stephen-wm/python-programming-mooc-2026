def sum_of_positives(my_list: list):
    sum = 0
 
    for number in my_list:
        if number > 0:
            sum = sum + number
 
    return sum
 
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)