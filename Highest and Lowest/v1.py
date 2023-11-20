def high_and_low(numbers):
    numbers = sorted(map(int, numbers.split(" ")), reverse=True)
    return str(numbers[0]) + " " + str(numbers[-1])
