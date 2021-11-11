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


def make_expr(a, b, calc):
    expr = ""
    i = 0
    while i < len(calc):
        if calc[i] == "A":
            expr += str(a)
        elif calc[i] == "B":
            expr += str(b)
        elif calc[i:i+2] == "or":
            expr += "f_or"
            i += 1
        elif calc[i:i+3] == "and":
            expr += "f_and"
            i += 2
        elif calc[i:i+3] == "not":
            expr += "f_not"
            i += 2
        elif calc[i:i+3] == "nor":
            expr += "f_nor"
            i += 2
        elif calc[i:i+3] == "xor":
            expr += "f_xor"
            i += 2
        elif calc[i:i+3] == "equ":
            expr += "f_equ"
            i += 2
        elif calc[i:i+4] == "nand":
            expr += "f_nand"
            i += 3
        elif calc[i:i+4] == "impl":
            expr += "f_impl"
            i += 3
        else:
            expr += calc[i]
        i += 1
    return expr


# P46: Evaluates logical expressions.
#       You can only evaluate expressions of the form (A or B) and not (A or B or B) (at maximum two inputs per function).
def p46(a, b, expr):
    res = eval(make_expr(a, b, expr))
    return res


# P46: Truth table for logic expression.
#       You can only evaluate expressions of the form (A or B) and not (A or B or B) (at maximum two inputs per function).
def p46tt(expr):
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

    print("---- " + str(expr) + " ----")
    print("a b x")
    a, b = 0, 0
    x = p46(a, b, expr)
    print(a, b, x)
    a, b = 0, 1
    x = p46(a, b, expr)
    print(a, b, x)
    a, b = 1, 0
    x = p46(a, b, expr)
    print(a, b, x)
    a, b = 1, 1
    x = p46(a, b, expr)
    print(a, b, x)


if __name__ == "__main__":
    p46tt("and(A, or(A, B))")
