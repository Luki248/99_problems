#!/usr/bin/env python3


# P21: Insert an element at a given position into a list.
def p21(insert, list, k):
    if list == []:
        return None
    else:
        return list[:k-1] + [insert] + list[k-1:]


if __name__ == "__main__":
    ret = p21(6, [1, 2, 3, 4], 2)
    print(ret)
