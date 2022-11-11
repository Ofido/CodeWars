# não deu certo
import math


def countZeros(n:str, length:int):
    aux = int(length / 5) # -> interessante que eu cheguei a essa conclusão sozinho. e eu usei isso de base quando pesquisei mais sobre as propriedades do fatorial
    cnt = aux
    print(n, length, aux, cnt)
    for num in n[aux:]:
        if int(num):
            break
        cnt += 1
    print(n, length, aux, cnt)
    if cnt == aux:
        for idx, num in enumerate(n[:aux]):
            if not int(num):
                cnt = idx + 1
    print(n, length, aux, cnt)
    return cnt

def zeros(n):
    return countZeros(str(math.factorial(n))[::-1], n)
