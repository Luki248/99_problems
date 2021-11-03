#!/usr/bin/env python3


# P20: Remove the K'th element from a list.
def p20(list, k):
    if list == []:
        return None
    else:
        return list[:k-1] + list[k:]


if __name__ == "__main__":
    ret = p20([1, 2, 3, 4], 2)
    print(ret)
