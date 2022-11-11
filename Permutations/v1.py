def permutations(s):
    if len(s) == 1: return [s]
    if len(s) == 2: return list(set([s[0]+s[1], s[1]+s[0]]))
    # montando lista de saida para facilitar o algoritimo
    saida = []

    def heap(lista:list, tamanho:int):
        if tamanho == 1: return saida.append(''.join(lista)) # retornando o append para simplifiacr o código, mesmo não sendo nescessário
        # aplicando a tranformação
        for i in range(tamanho):
            heap(lista, tamanho-1) # recursividade
            if tamanho & 1:
                lista[0], lista[tamanho-1] = lista[tamanho-1], lista[0]
            else:
                lista[i], lista[tamanho-1] = lista[tamanho-1], lista[i]
    heap([letra for letra in s], len(s)) # executando a função
    print('aaaaaaaa')
    return list(set(saida))

if __name__ == '__main__':
    a = permutations('aa')
    a.sort()
    print(a)
