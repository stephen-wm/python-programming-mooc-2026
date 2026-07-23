def largest() -> int:
    largest_num = 0

    with open("numbers.txt") as file:
        for number in file:
            if int(number) > largest_num:
                largest_num = int(number)

    return largest_num
