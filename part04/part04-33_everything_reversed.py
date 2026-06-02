def everything_reversed(my_list: list):
    return_list = []

    for item in my_list:
        return_list.append(item[::-1])

    # alternative return statement => return return_list[len(return_list)-1::-1]
    return return_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)