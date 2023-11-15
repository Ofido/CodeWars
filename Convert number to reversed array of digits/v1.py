def digitize(n):
    return list(map(int, str(n)[::-1]))


if __name__ == "__main__":
    print(digitize(int(input())))
