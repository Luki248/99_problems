#!/usr/bin/env python3

import p22
import p23


# P24: Lotto: Draw N different random numbers from the set 1..M.
def p24(count, limit):
    return p23.p23(p22.p22(1, limit), count)


if __name__ == "__main__":
    ret = p24(6, 49)
    print(ret)
