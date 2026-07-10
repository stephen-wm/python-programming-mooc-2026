def factorials(n: int):
    numbers = {}
    result = 1

    for i in range(1, n + 1):
        result *= i
        numbers[i] = result

    return numbers
