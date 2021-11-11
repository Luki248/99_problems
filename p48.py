#!/usr/bin/env python3


import p46


def lexer_universal(variables, expr):
    func = []
    i = 0
    while i < len(expr):
        if expr[i] == " ":
            ...  # do nothing
        elif expr[i] == "(":
            func.append("(")
        elif expr[i] == ")":
            func.append(")")
        elif (expr[i] >= "A") and (expr[i] <= "Z"):
            func.append(str(variables[ord(expr[i]) - ord("A")]))
        elif expr[i:i+2] == "or":
            func.append("p46.f_or")
            i += 1
        elif expr[i:i+3] == "and":
            func.append("p46.f_and")
            i += 2
        elif expr[i:i+3] == "not":
            func.append("p46.f_not")
            i += 2
        elif expr[i:i+3] == "nor":
            func.append("p46.f_nor")
            i += 2
        elif expr[i:i+3] == "xor":
            func.append("p46.f_xor")
            i += 2
        elif expr[i:i+3] == "equ":
            func.append("p46.f_equ")
            i += 2
        elif expr[i:i+4] == "nand":
            func.append("p46.f_nand")
            i += 3
        elif expr[i:i+4] == "impl":
            func.append("p46.f_impl")
            i += 3
        else:
            print("Unknown Character!")
        i += 1
    return func


def find_matching_parentheses(func):
    parentheses = []
    i = 0
    while i < len(func):
        if func[i] == "(":
            j = i + 1
            count = 1
            while j < len(func):
                if func[j] == "(":
                    count += 1
                elif func[j] == ")":
                    count -= 1
                if count == 0:
                    parentheses.append([i, j])
                    break
                j += 1
        i += 1
    return parentheses


def mover(func):
    calc = []
    i = 0
    while i < len(func):
        if func[i] == "(":
            if func[i+1] == "p46.f_not":
                calc.append(func[i+1])
                calc.append(func[i])
                calc.append(func[i+2])
                calc.append(")")
                i += 2
            else:
                calc.append(func[i+2])
                calc.append(func[i])
                calc.append(func[i+1])
                calc.append(",")
                i += 2
        elif func[i] == ")":
            if func[i-2] == "p46.f_not":
                ...  # do nothing
            else:
                calc.append(")")
        else:
            calc.append(func[i])
        i += 1
    return calc


def combine_list_to_str(calc):
    expr = ""
    for item in calc:
        expr += item
    return expr


def evaluate(expr):
    #print(expr)
    if len(expr) == 1:
        return expr[0]
    else:
        parentheses = find_matching_parentheses(expr)
        if len(parentheses) == 0:
            expr.insert(0, "(")
            expr.append(")")
            expression = mover(expr)
            expr_as_string = combine_list_to_str(expression)
            return int(eval(expr_as_string))
        else:
            par_start = parentheses[-1][0] + 1
            par_end = parentheses[-1][1]
            ret1 = int(evaluate(expr[par_start:par_end]))
            new_expr = expr[0:par_start-1] + [str(ret1)] + expr[par_end+1:]
            return int(evaluate(new_expr))


# P48: Evaluates logical expressions (3).
#       You can only evaluate expressions of the form (A or B) and not (A or B or B) (at maximum two inputs per function).
#       And only in the form (A and (A or B)) and not ((A or B) and A).
def p48(variables, expr):
    func = lexer_universal(variables, expr)
    return evaluate(func)


# P48: Truth tables for logical expressions (3).
#       You can only evaluate expressions of the form (A or B) and not (A or B or B) (at maximum two inputs per function).
#       And only in the form (A and (A or B)) and not ((A or B) and A).
def p48tt(variables, expr):
    print("---- " + str(expr) + " ----")
    for i in range(len(variables)):
        print(chr(ord("A") + i) + " ", end="")
    print("x")
    for i in range(2**len(variables)):
        args = []
        for j in range(len(variables)-1, -1, -1):
            value = (i >> j) & 1
            args.append(value)
            print(str(value) + " ", end="")
        print(p48(args, expr))


if __name__ == "__main__":
    p48tt([1, 0, 0], "((A and (B or C)) equ ((A and B) or (A and C)))")
