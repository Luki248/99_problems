#!/usr/bin/env python3


import p46


def lexer(expr):
    func = []
    i = 0
    while i < len(expr):
        if expr[i] == " ":
            ...  # do nothing
        elif expr[i] == "(":
            func.append("(")
        elif expr[i] == ")":
            func.append(")")
        elif expr[i] == "A":
            func.append("A")
        elif expr[i] == "B":
            func.append("B")
        elif expr[i:i+2] == "or":
            func.append("or")
            i += 1
        elif expr[i:i+3] == "and":
            func.append("and")
            i += 2
        elif expr[i:i+3] == "not":
            func.append("not")
            i += 2
        elif expr[i:i+3] == "nor":
            func.append("nor")
            i += 2
        elif expr[i:i+3] == "xor":
            func.append("xor")
            i += 2
        elif expr[i:i+3] == "equ":
            func.append("equ")
            i += 2
        elif expr[i:i+4] == "nand":
            func.append("nand")
            i += 3
        elif expr[i:i+4] == "impl":
            func.append("impl")
            i += 3
        else:
            print("Unknown Character!")
        i += 1
    return func


def mover(func):
    calc = []
    i = 0
    while i < len(func):
        if func[i] == "(":
            if func[i+1] == "not":
                calc.append(func[i+1])
                calc.append(func[i])
                calc.append(func[i+2])
                calc.append(")")
            else:
                calc.append(func[i+2])
                calc.append(func[i])
                calc.append(func[i+1])
                calc.append(",")
        elif func[i] == ")":
            if func[i-2] == "not":
                ...  # do nothing
            else:
                calc.append(")")
        i += 1
    return calc


def combine_list_to_str(calc):
    expr = ""
    for item in calc:
        expr += item
    return expr


# P47: Evaluates logical expressions (2).
#       You can only evaluate expressions of the form (A or B) and not (A or B or B) (at maximum two inputs per function).
def p47(a, b, expr):
    #print(expr)
    func = lexer(expr)
    #print(func)
    calc = mover(func)
    #print(calc)
    expression = combine_list_to_str(calc)
    #print(expression)
    ret = p46.p46(a, b, expression)
    return ret


# P47: Truth table for logic expression (2).
#       You can only evaluate expressions of the form (A or B) and not (A or B or B) (at maximum two inputs per function).
def p47tt(expr):
    print("---- " + str(expr) + " ----")
    print("a b x")
    a, b = 0, 0
    x = p47(a, b, expr)
    print(a, b, x)
    a, b = 0, 1
    x = p47(a, b, expr)
    print(a, b, x)
    a, b = 1, 0
    x = p47(a, b, expr)
    print(a, b, x)
    a, b = 1, 1
    x = p47(a, b, expr)
    print(a, b, x)


if __name__ == "__main__":
    p47tt("(A and (A or (not B)))")
