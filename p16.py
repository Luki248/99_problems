#!/usr/bin/env python3


# P16: Drop every N'th element from a list.
def p16(list, k):
    if list == []:
        return None
    else:
        new_list = []
        for i in range(len(list)):
            if i % k != (k-1):
                new_list.append(list[i])
        return new_list


if __name__ == "__main__":
    ret = p16([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(ret)
