#!/usr/bin/env python3


# P32: Determine the greatest common divisor of two positive integer numbers.
def p32(m, n):
    if input < 1:
        return None
    else:
        for i in range((input - 1), 1, -1):
            if input % i == 0:
                return False
        return True


if __name__ == "__main__":
    ret = p32(24, 6)
    print(ret)
