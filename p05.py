#!/usr/bin/env python3


# P05: Reverse a list.
def p05(list):
    list.reverse()
    return list

if __name__ == "__main__":
    ret = p05([1,2,3,4])
    print(ret)