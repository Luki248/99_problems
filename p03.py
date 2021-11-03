#!/usr/bin/env python3


# P03: Find the K'th element of a list.
def p03(list, k):
    l = len(list)
    if l == 0:
        return None
    elif l <= k:
        return None
    else:
        return list[k]


if __name__ == "__main__":
    ret = p03([1, 2, 3, 4], 3)
    print(ret)
