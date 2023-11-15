def multiples_of(numbers: list, of: int):
    return [n for n in numbers if not n % of]


def solution(number: int):
    output = 0
    if number <= 3:
        return output
    output += 3
    if number <= 5:
        return output
    output += 5
    if number == 6:
        return output
    numbers = list(range(6, number))
    return output + sum(
        set(multiples_of(numbers, 3) + multiples_of(numbers, 5))
    )


if __name__ == "__main__":
    print(solution(int(input())))
