#!/usr/bin/env python3


# P02: Find the last but one box of a list.
def p02(list):
    if len(list) < 2:
        return None
    else:
        return [list[-2], list[-1]]

if __name__ == "__main__":
    ret = p02([1,2,3,4])
    print(ret)