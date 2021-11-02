#!/usr/bin/env python3

# P01: Find the last box of a list.

def p01(list):
    return list[-1]

if __name__ == "__main__":
    ret = p01([1,2,3,4])
    print(ret)