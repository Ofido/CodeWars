from math import sqrt

positive = lambda a,b,c: (-1 * b + sqrt(b*b - 4*a*c))/2*a
negative = lambda a,b,c: (-1 * b - sqrt(b*b - 4*a*c))/2*a

def solver(a, b, c):
    return list(set([positive(a,b,c), negative(a,b,c)]))
