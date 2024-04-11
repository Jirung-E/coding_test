expr = input()
stack = []

for e in expr:
    if e in ['-', '+']:
        stack.append("(" + stack.pop(-2) + e + stack.pop(-1) + ")")
    else:
        stack.append(e)
    # print(stack)

print(stack[0])


# ab+cd+e-a+-
#
# ['a']
# ['a', 'b']
# ['(a+b)']
# ['(a+b)', 'c']
# ['(a+b)', 'c', 'd']
# ['(a+b)', '(c+d)']
# ['(a+b)', '(c+d)', 'e']
# ['(a+b)', '((c+d)-e)']
# ['(a+b)', '((c+d)-e)', 'a']
# ['(a+b)', '(((c+d)-e)+a)']
# ['((a+b)-(((c+d)-e)+a))']