#!/usr/bin/env python3


# P32: Determine the greatest common divisor of two positive integer numbers.
def p32(m, n):
    if n == 0:
        return m
    else:
        return p32(n, m % n)


if __name__ == "__main__":
    ret = p32(36, 63)
    print(ret)
