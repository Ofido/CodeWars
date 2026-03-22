def regule(num: str) -> int:
    if num == "":
        return 1
    if num == "-":
        return -1
    return int(num)


def differentiate(equation: str, point: int) -> int:
    list_poly: list[str] = [
        t for t in equation.replace("-", "+-").split("+") if t
    ]
    output = 0
    for poly in list_poly:
        if "x" in poly:  # ignoro contante
            if "^" in poly:  # caso 3
                a, n = poly.split("x^")
                output += regule(a) * regule(n) * point ** (regule(n) - 1)
                continue
            output += regule(poly[:-1])

    return output
