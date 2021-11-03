#!/usr/bin/env python3


# P18: Extract a slice from a list.
def p18(list, j, k):
    if list == []:
        return None
    else:
        return list[j-1:k]


if __name__ == "__main__":
    ret = p18([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7)
    print(ret)
