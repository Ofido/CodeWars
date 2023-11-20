def high_and_low(numbers):
    return " ".join(x(numbers.split(), key=int) for x in (max, min))
