import itertools
def permutations(s):
    return [] if len(s) == 0 else [s] if len(s) == 1 else list("".join(p) for p in set(itertools.permutations(s)))

if __name__ == '__main__':
    a = permutations('aa')
    a.sort()
    print(a)
