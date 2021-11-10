#!/usr/bin/env python3


import p33


# P34: Calculate Euler's totient function phi(m).
def p34(m):
    if m < 1:
        return None
    else:
        count = 0
        for i in range(1, m):
            if p33.p33(i, m) == True:
                count += 1
        return count


if __name__ == "__main__":
    ret = p34(315)
    print(ret)
