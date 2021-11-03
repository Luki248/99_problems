#!/usr/bin/env python3

import random
import p20


# P23: Extract a given number of randomly selected elements from a list.
def p23(input, k):
    if input == []:
        return None
    else:
        new_list = []
        for _ in range(k):
            index = random.randint(0, len(input) - 1)
            item = input[index]
            input = p20.p20(input, index + 1)
            new_list.append(item)
        return new_list


if __name__ == "__main__":
    ret = p23([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(ret)
