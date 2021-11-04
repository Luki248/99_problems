#!/usr/bin/env python3


# P22: Create a list containing all integers within a given range.
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
