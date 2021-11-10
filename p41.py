#!/usr/bin/env python3


import p40


# P41: A list of Goldbach compositions.
def p41(m, n):
    if m < 1:
        return None
    if n < 1:
        return None
    else:
        if n < m:
            t = m
            m = n
            n = t
        result = []
        for i in range(m, n + 1):
            if i % 2 == 0:
                gconj = p40.p40(i)
                result.append(str(i) + "=" + str(gconj[0]) + "+" + str(gconj[1]))
        return result


if __name__ == "__main__":
    ret = p41(9, 20)
    print(ret)
