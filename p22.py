#!/usr/bin/env python3


# P22: Insert an element at a given position into a list.
def p22(j, k):
    if j < k:
        return list(range(j, k+1, 1))
    elif j > k:
        return list(range(j, k-1, -1))
    else:
        return None


if __name__ == "__main__":
    ret = p22(4, 9)
    print(ret)
