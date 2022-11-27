#!/usr/bin/env python3

import p26
import p54A

SYMBOl = "x"

# 0: [SYMBOl, None, None]
# 1: [SYMBOl, []  , None]
# 2: [SYMBOl, None, []  ]
# 3: [SYMBOl, [],   []  ]


def generate_permutations(list):
    return p26.heap_algorithm(len(list), list)

def complete_balanced_tree(list, k):
    ret = []
    if k > 1:
        ret.append([SYMBOl, complete_balanced_tree(list[:k-1][0], k-1), None])
        ret.append([SYMBOl, None, complete_balanced_tree(list[:k-1][0], k-1)])
        ret.append([SYMBOl, complete_balanced_tree(list[:k-1][0], k-2), complete_balanced_tree(list[:k-1][0], k-2)])
        return ret
    return list


# P55: Construct completely balanced binary trees.
def p55(k):
    nodes = k*[[SYMBOl, None, None]]

    return complete_balanced_tree(nodes, k)
    if list == None:
        return True
    if list == []:
        return False
    else:
        return False
    


if __name__ == "__main__":
    ret = p55(3)
    print(ret)


    for btree in ret:
        print(btree, p54A.p54A(btree))
