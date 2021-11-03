#!/usr/bin/env python3

import p09

# P11: Modified run-length encoding.
def p11(list):
    if list == []:
        return None
    else:
        list = p09.p09(list)
        new_list = []
        for item in list:
            if len(item) == 1:
                temp = item[0]
            else:
                temp = [len(item), item[0]]
            new_list.append(temp)
        return new_list


if __name__ == "__main__":
    ret = p11([1, 2, 2, 3, 1, 5, 5, 5, 5])
    print(ret)
