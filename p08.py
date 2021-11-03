#!/usr/bin/env python3


# P08: Eliminate consecutive duplicates of list elements.
def p08(list):
    if list == []:
        return None
    else:
        new_list = []
        new_list.append(list[0])
        i_new = 0
        for i in range(len(list)):
            if list[i] != new_list[i_new]:
                new_list.append(list[i])
                i_new += 1
        return new_list


if __name__ == "__main__":
    ret = p08([1, 2, 2, 3, 1, 5, 5, 5, 5])
    print(ret)
