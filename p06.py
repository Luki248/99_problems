#!/usr/bin/env python3


# P06: Find out whether a list is a palindrome.
def p06(list):
    if list == []:
        return None
    else:
        for i in range(len(list)):
            if list[i] != list[len(list) - i - 1]:
                return False
        return True


if __name__ == "__main__":
    ret = p06([1, 2, 1])
    print(ret)
