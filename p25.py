#!/usr/bin/env python3

import p23


# P25: Generate a random permutation of the elements of a list.
def p25(input):
    if input == []:
        return None
    else:
        new_list = []
        for _ in range(len(input)):
            item = p23.p23(input, 1)[0]
            new_list.append(item)
            input.remove(item)
        return new_list


if __name__ == "__main__":
    ret = p25([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(ret)
