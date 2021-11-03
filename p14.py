#!/usr/bin/env python3


# P14: Duplicate the elements of a list.
def p14(list):
    if list == []:
        return None
    else:
        new_list = []
        for item in list:
            new_list.append(item)
            new_list.append(item)
        return new_list


if __name__ == "__main__":
    ret = p14([1, 2, 3, 4])
    print(ret)
