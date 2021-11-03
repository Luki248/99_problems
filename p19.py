#!/usr/bin/env python3


# P19: Rotate a list N places to the left.
def p19(list, k):
    if list == []:
        return None
    else:
        new_list = []
        for i in range(len(list)):
            index = (i + k) % len(list)
            new_list.append(list[index])
        return new_list


if __name__ == "__main__":
    ret = p19([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(ret)
