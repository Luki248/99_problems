#!/usr/bin/env python3


import p32


# P33: Determine whether two positive integer numbers are coprime.
def p33(m, n):
    if p32.p32(m, n) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    ret = p33(35, 64)
    print(ret)
