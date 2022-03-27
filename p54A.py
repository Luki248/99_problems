#!/usr/bin/env python3


# P54A: Check whether a given expression represents a binary tree.
def p54A(list):
    if list == None:
        return True
    if list == []:
        return False
    elif len(list) > 2 and not(len(list) % 3):
        if p54A(list[1]) == True and p54A(list[2]) == True:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    ret = p54A(["a", ["b", None, None], None])
    print(ret)
