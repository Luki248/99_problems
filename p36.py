#!/usr/bin/env python3


import p35


def p13(list):  # it is P13 with the item and the counts reversed
    if list == []:
        return None
    else:
        new_list = []
        old_element = list[0]
        count_same_element = 0
        for item in list:
            if item == old_element:
                count_same_element += 1
            else:
                temp = [old_element, count_same_element]
                new_list.append(temp)
                old_element = item
                count_same_element = 1
        temp = [old_element, count_same_element]
        new_list.append(temp)
        return new_list


# P36: Determine the prime factors of a given positive integer (2).
def p36(m):
    if m < 1:
        return None
    else:
        return p13(p35.p35(m))


if __name__ == "__main__":
    ret = p36(315)
    print(ret)
