#!/usr/bin/env python3


# P13: Run-length encoding of a list (direct solution).
def p13(list):
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
                temp = [count_same_element, old_element]
                new_list.append(temp)
                old_element = item
                count_same_element = 1
        temp = [count_same_element, old_element]
        new_list.append(temp)
        return new_list


if __name__ == "__main__":
    ret = p13([1, 2, 2, 3, 1, 5, 5, 5, 5])
    print(ret)
