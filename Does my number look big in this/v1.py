def narcissistic(value):
    result = 0
    value_str = str(value)
    digits = len(value_str)
    for a in [int(a) for a in value_str]:
        result += a**digits
    return result == value
