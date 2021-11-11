#!/usr/bin/env python3


# P49: Gray code.
def p49(m):
    code = []
    for i in range(0, 2**m):
        new = i ^ (i >> 1)
        code.append("{:03b}".format(new))
    return code


if __name__ == "__main__":
    ret = p49(3)
    print(ret)
