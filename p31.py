#!/usr/bin/env python3


# P31: Determine whether a given integer number is prime.
def p31(input):
    if input < 1:
        return None
    else:
        for i in range((input - 1), 1, -1):
            if input % i == 0:
                return False
        return True


if __name__ == "__main__":
    ret = p31(112)
    print(ret)
