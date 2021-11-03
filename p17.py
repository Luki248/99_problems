#!/usr/bin/env python3


# P17: Split a list into two parts; the length of the first part is given.
def p17(list, k):
    if list == []:
        return None
    else:
        return [list[:3], list[3:]]


if __name__ == "__main__":
    ret = p17([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(ret)
