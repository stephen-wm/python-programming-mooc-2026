def dict_of_numbers() -> dict:
    ones = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    teens = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    dictionary = {}

    for number in range(100):
        if number < 10:
            dictionary[number] = ones[number]
        elif number < 20:
            dictionary[number] = teens[number]
        else:
            tens_place = number // 10
            ones_place = number % 10
            if ones_place == 0:
                dictionary[number] = tens[tens_place]
            else:
                dictionary[number] = f"{tens[tens_place]}-{ones[ones_place]}"
                # can also concatenate strings like this
                # dictionary[number] = tens[tens_place] + "-" + ones[ones_place]

    return dictionary

if __name__ == "__main__":
    numbers = dict_of_numbers()

    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])