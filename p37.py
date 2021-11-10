#!/usr/bin/env python3


import p36


# P37: Calculate Euler's totient function phi(m) (improved).
def p37(m):
    if m < 1:
        return None
    else:
        primes = p36.p36(m)
        phi = 1
        for p, m in primes:
            phi *= (p - 1) * (p ** (m - 1))
        return phi


if __name__ == "__main__":
    ret = p37(315)
    print(ret)
