#!/usr/bin/env python3


# P15: Replicate the elements of a list a given number of times.
def p15(list, k):
    if list == []:
        return None
    else:
        new_list = []
        for item in list:
            for _ in range(k):
                new_list.append(item)
        return new_list


if __name__ == "__main__":
    ret = p15([1, 2, 3, 4], 3)
    print(ret)
