#!/usr/bin/env python3


# P09: Pack consecutive duplicates of list elements into sublists.
def p09(list):
    if list == []:
        return None
    else:
        new_list = []
        temp_list = []
        old_element = list[0]
        for i in range(len(list)):
            if list[i] == old_element:
                temp_list.append(list[i])
            else:
                new_list.append(temp_list.copy())
                temp_list = [list[i]]
                old_element = list[i]
        new_list.append(temp_list.copy())
        return new_list


if __name__ == "__main__":
    ret = p09([1, 2, 2, 3, 1, 5, 5, 5, 5])
    print(ret)
