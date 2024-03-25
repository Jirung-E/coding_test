operators = ['-', '+']

expr = [c for c in input()]

while True:
    for i in range(len(expr)-1, 1, -1):
        if expr[i] in operators:
            if expr[i-1] not in operators and expr[i-2] not in operators:
                expr[i-2] = "(" + expr[i-2] + expr[i] + expr[i-1] + ")"
                expr.pop(i-1)
                expr.pop(i-1)
                i = i-2
    if len(expr) == 1:
        break

print(expr[0])


# ["a", "b", "+", "c", "d", "+", "e", "-", "a", "+", "-"]
# ["(a+b)", "(c+d)", "e", "-", "a", "+", "-"]
# ["(a+b)", "((c+d)-e)", "a", "+", "-"]
# ["(a+b)", "(((c+d)-e)+a)", "-"]
# ["((a+b)-(((c+d)-e)+a))"]