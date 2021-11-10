#!/usr/bin/env python3


import p39


# P40: Goldbach's conjecture.
def p40(m):
    if m < 1:
        return None
    else:
        primes = p39.p39(1, m)
        for i in range(0, len(primes)):
            if i != 0:
                if primes.count(m - primes[i]) == 1:
                    return [primes[i], m - primes[i]]


if __name__ == "__main__":
    ret = p40(20)
    print(ret)
