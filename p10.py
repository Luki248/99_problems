#!/usr/bin/env python3

import p09

# P10: Run-length encoding of a list.
def p10(list):
    if list == []:
        return None
    else:
        list = p09.p09(list)
        new_list = []
        for item in list:
            temp = [len(item), item[0]]
            new_list.append(temp)
        return new_list


if __name__ == "__main__":
    ret = p10([1, 2, 2, 3, 1, 5, 5, 5, 5])
    print(ret)
