def calc_1(x: int) -> int:
    return 2 * x + 1


def calc_2(x: int) -> int:
    return 3 * x + 1


def dbl_linear(n: int):
    l: list[int] = [1]
    cnt = 0
    i2 = 0
    i3 = 0
    c2 = 0
    c3 = 0
    while True:
        if c2 == 0:
            c2 = calc_1(l[i2])
        if c3 == 0:
            c3 = calc_2(l[i3])
        if c2 == c3:
            l.append(c2)
            c2, c3 = 0, 0
            i2 += 1
            i3 += 1
        elif c2 < c3:
            l.append(c2)
            c2 = 0
            i2 += 1
        else:
            l.append(c3)
            c3 = 0
            i3 += 1
        cnt += 1
        if cnt == n:
            break
    return l[n]


print(dbl_linear(10) == 22)
print(dbl_linear(20) == 57)
print(dbl_linear(30) == 91)
print(dbl_linear(50) == 175)
