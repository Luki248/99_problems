#!/usr/bin/env python3


# P35: Determine the prime factors of a given positive integer.
def p35(m):
    if m < 1:
        return None
    else:
        factors = []
        divident = m
        i = 2
        while divident > 1:
            if (divident % i) == 0:
                factors.append(i)
                divident /= i
            else:
                i += 1
        return factors


if __name__ == "__main__":
    ret = p35(315)
    print(ret)
