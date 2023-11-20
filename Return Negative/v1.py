def make_negative(number):
    if number <= 0:
        return number
    return number * -1


# other solution is tu use abs function to get que number relative position at
# 0 point and turn it negative: only return -abs(number)
# or else better only do: return -number if number >0 else number
