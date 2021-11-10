#!/usr/bin/env python3


import p34
import p37
import time


# P38: Compare the two methods of calculating Euler's totient function.
#       Analyse the runtime of the two functions.
def p38(m):
    if m < 1:
        return None
    else:
        start = time.perf_counter()
        p34.p34(m)
        time_p34 = time.perf_counter() - start
        start = time.perf_counter()
        p37.p37(m)
        time_p37 = time.perf_counter() - start
        return time_p34, time_p37


if __name__ == "__main__":
    ret = p38(10090)
    print(ret)
