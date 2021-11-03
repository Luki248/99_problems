#!/usr/bin/env python3


# P07: Flatten a nested list structure.
def p07(list):
    if list == None:
        return []
    elif list == []:
        return None
    elif type(list) != type([]):
        return list
    elif len(list) == 1:
        return list[0]
    else:
        new_list = []
        res1 = p07(list[0])
        res2 = p07(list[1:])
        if type(res1) != type([]):
            new_list.append(res1)
        else:
            new_list = new_list + res1
        if type(res2) != type([]):
            new_list.append(res2)
        else:
            new_list = new_list + res2
        return new_list


if __name__ == "__main__":
    ret = p07([1, 2, [31, 32], [41, [42, 43]], 5])
    print(ret)
