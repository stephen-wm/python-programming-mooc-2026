def times_ten(start_index: int, end_index: int):
    numbers = {}
    for i in range(start_index, end_index + 1):
        numbers[i] = i * 10
    return numbers
