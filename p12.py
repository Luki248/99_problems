#!/usr/bin/env python3


# P12: Decode a run-length encoded list.
def p12(list):
    if list == []:
        return None
    else:
        new_list = []

        for item in list:
            if type(item) == type([]):
                item_counts = item[0]
                item_type = item[1]
                for _ in range(item_counts):
                    new_list.append(item_type)
            else:
                new_list.append(item)
        return new_list


if __name__ == "__main__":
    ret = p12([1, [2, 2], 3, 1, [4, 5]])
    print(ret)
