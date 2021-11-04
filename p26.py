#!/usr/bin/env python3

import p23


def swap(input, m, n):
    new_list = input.copy()
    new_list[m] = input[n]
    new_list[n] = input[m]
    return new_list


def heap_algorithm(k, input):
    if k < 2:
        # print(input)
        return [input]
    else:
        ret = []
        ret += heap_algorithm(k - 1, input)
        for i in range(0, k - 1):
            if k % 2 == 1:
                new_list = swap(input, i, k - 1)
            else:
                new_list = swap(input, 0, k - 1)
            ret += heap_algorithm(k - 1, new_list)
        return ret


# P26: Generate the combinations of K distinct objects chosen from the N elements of a list
def p26(k, input):
    if input == []:
        return None
    elif k < 1:
        return None
    else:
        all_combinations = heap_algorithm(len(input), input)
        return p23.p23(all_combinations, k)


if __name__ == "__main__":
    ret = p26(3, [1, 2, 3, 4])
    print(ret)
