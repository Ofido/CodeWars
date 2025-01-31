def beggars(values, n):
    return [sum(values[i] for i in range(j, len(values), n)) for j in range(n)] if n > 0 else []

def beggars(values, n):
    if n == 0:
        return []

    # Usar uma lista ao invés de um dicionário para simplificar
    out = [0] * n

    # Iterar sobre valores juntamente com índices
    for idx, value in enumerate(values):
        out[idx % n] += value

    return out
    # Usar uma lista ao invés de um dicionário para simplificar
    out = [0] * n

    # Iterar sobre valores juntamente com índices
    for idx, value in enumerate(values):
        out[idx % n] += value

    return out
