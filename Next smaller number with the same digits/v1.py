from itertools import permutations

# ainda não concluído


def next_smaller(n):
    n_str = str(n)
    result = min(
        *(
            int(("%d" * len(n_str)) % x) if x[0] != 0 else int("9" * len(n_str))
            for x in permutations(list(map(int, n_str)), len(n_str))
        )
    )
    return result if result != n else -1


if __name__ == "__main__":
    print(next_smaller(230))
