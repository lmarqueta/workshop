#!/usr/bin/env python
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Uso: {} num modulo\n".format(sys.argv[0]))
        sys.exit(1)
    e = sys.argv[1]
    mod = sys.argv[2]
    print mulinv(long(e), long(mod))
