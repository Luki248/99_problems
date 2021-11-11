#!/usr/bin/env python3


def f_not(x):
    return int(not x)


def tt_not():
    print("a x")
    a = 0
    x = f_not(a)
    print(a, x)
    a = 1
    x = f_not(a)
    print(a, x, "\n")


def f_and(x, y):
    return int(x and y)


def tt_and():
    print("a b x")
    a, b = 0, 0
    x = f_and(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_and(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_and(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_and(a, b)
    print(a, b, x, "\n")


def f_or(x, y):
    return int(x or y)


def tt_or():
    print("a b x")
    a, b = 0, 0
    x = f_or(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_or(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_or(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_or(a, b)
    print(a, b, x, "\n")


def f_nand(x, y):
    return int(not (x and y))


def tt_nand():
    print("a b x")
    a, b = 0, 0
    x = f_nand(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_nand(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_nand(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_nand(a, b)
    print(a, b, x, "\n")


def f_nor(x, y):
    return int(not (x or y))


def tt_nor():
    print("a b x")
    a, b = 0, 0
    x = f_nor(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_nor(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_nor(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_nor(a, b)
    print(a, b, x, "\n")


def f_xor(x, y):
    return int(f_and(f_nand(x, y), f_or(x, y)))


def tt_xor():
    print("a b x")
    a, b = 0, 0
    x = f_xor(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_xor(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_xor(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_xor(a, b)
    print(a, b, x, "\n")


def f_equ(x, y):
    return int(f_not(f_xor(x, y)))


def tt_equ():
    print("a b x")
    a, b = 0, 0
    x = f_equ(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_equ(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_equ(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_equ(a, b)
    print(a, b, x, "\n")


def f_impl(x, y):
    return int(f_or(f_not(x), y))


def tt_impl():
    print("a b x")
    a, b = 0, 0
    x = f_impl(a, b)
    print(a, b, x)
    a, b = 0, 1
    x = f_impl(a, b)
    print(a, b, x)
    a, b = 1, 0
    x = f_impl(a, b)
    print(a, b, x)
    a, b = 1, 1
    x = f_impl(a, b)
    print(a, b, x, "\n")


# P46: Truth tables for logical expressions.
def p46():
    print("---- not ----")
    tt_not()

    print("---- and ----")
    tt_and()

    print("---- or ----")
    tt_or()

    print("---- nand ----")
    tt_nand()

    print("---- nor ----")
    tt_nor()

    print("---- xor ----")
    tt_xor()

    print("---- equ ----")
    tt_equ()

    print("---- impl ----")
    tt_impl()

    print("---- (A and (A or B)) ----")
    print("a b x")
    a, b = 0, 0
    x = f_and(a, f_or(a, b))
    print(a, b, x)
    a, b = 0, 1
    x = f_and(a, f_or(a, b))
    print(a, b, x)
    a, b = 1, 0
    x = f_and(a, f_or(a, b))
    print(a, b, x)
    a, b = 1, 1
    x = f_and(a, f_or(a, b))
    print(a, b, x)


if __name__ == "__main__":
    p46()
