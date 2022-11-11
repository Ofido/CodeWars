# https://math.stackexchange.com/questions/286947/number-of-zero-digits-in-factorials
# https://www.handakafunda.com/number-of-trailing-zeros/
def zeros(n):
    aux = 0
    while n >= 5:
        n = int(n / 5)
        aux += n
    return aux
