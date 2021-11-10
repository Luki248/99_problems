#!/usr/bin/env python3


import p31


# P39: A list of prime numbers.
def p39(m, n):
    if m < 1:
        return None
    elif n < 1:
        return None
    else:
        if n < m:
            t = m
            m = n
            n = t
        primes = []
        for i in range(m, n):
            if p31.p31(i):
                primes.append(i)
        return primes


if __name__ == "__main__":
    ret = p39(10, 100)
    print(ret)
