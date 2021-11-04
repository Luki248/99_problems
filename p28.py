#!/usr/bin/env python3

import p26


def sort_length(list):
    return len(list)


# P28a: Sorting a list of lists according to length of sublists
#    a) We suppose that a list contains elements that are lists themselves.
#       The objective is to sort the elements of this list according to their length.
#       E.g. short lists first, longer lists later, or vice versa.
def p28a(input):
    if input == []:
        return None
    else:
        input.sort(key=sort_length)
        return input


# P28b: Sorting a list of lists according to length of sublists
#    b) Again, we suppose that a list contains elements that are lists themselves.
#       But this time the objective is to sort the elements of this list according to their length frequency;
#       i.e., in the default, where sorting is done ascendingly, lists with rare lengths are placed first,
#       others with a more frequent length come later.
def p28b(input):
    if input == []:
        return None
    else:
        list_lengths = []
        max_length = 0
        for list in input:
            len_of_list = len(list)
            list_lengths.append(len_of_list)
            if len_of_list > max_length:
                max_length = len_of_list

        count_of_same_lengths = []
        for _ in range(max_length + 1):
            count_of_same_lengths.append([])
        for i in range(0, len(list_lengths)):
            count_of_same_lengths[list_lengths[i]].append(i)

        new_list = []
        for i in range(len(count_of_same_lengths) - 1, -1, -1):
            item = count_of_same_lengths[i]
            for j in item:
                new_list.append(input[j])
        return new_list


if __name__ == "__main__":
    ret = p28a([[1, 2], [3], [4, 5, 6, 7], [], [8, 9]])
    print(ret)
    ret = p28b([[1, 2], [3], [4, 5, 6, 7], [], [8, 9]])
    print(ret)
