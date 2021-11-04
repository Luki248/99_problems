#!/usr/bin/env python3

import p26


# P27a: Group the elements of a set into disjoint subsets.
#    a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2, 3 and 4 persons?
#       Write a function that generates all the possibilities and returns them in a list.
def p27a(input):
    if input == []:
        return None
    else:
        all_combinations = p26.heap_algorithm(len(input), input)
        new_list = []
        for i in range(len(all_combinations)):
            temp = [all_combinations[i][0:2],
                    all_combinations[i][2:5],
                    all_combinations[i][5:9]]
            # print(temp)
            new_list.append(temp)
        return new_list


# P27b: Group the elements of a set into disjoint subsets.
#    b) Generalize the above predicate in a way that we can specify a list of group sizes and the predicate will return a list of groups.
def p27b(input, k, m, n):
    if input == []:
        return None
    elif k < 1:
        return None
    elif m < 1:
        return None
    elif n < 1:
        return None
    elif (k + m + n) != len(input):
        return None
    else:
        all_combinations = p26.heap_algorithm(len(input), input)
        new_list = []
        for i in range(len(all_combinations)):
            temp = [all_combinations[i][0:k],
                    all_combinations[i][k:m+k],
                    all_combinations[i][m+k:len(input)]]
            # print(temp)
            new_list.append(temp)
        return new_list


if __name__ == "__main__":
    ret = p27a([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(ret)
    ret = p27b([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 2, 5)
    print(ret)
