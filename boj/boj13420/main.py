TESTCASE = int(input())

for _ in range(TESTCASE):
    expr = input()
    n1, op, n2, _, res = expr.split()
    n1, n2, res = int(n1), int(n2), int(res)

    match op:
        case '+': 
            is_ok = n1 + n2 == res
        case '-': 
            is_ok = n1 - n2 == res
        case '*': 
            is_ok = n1 * n2 == res
        case '/': 
            is_ok = n1 // n2 == res

    print('correct' if is_ok else 'wrong answer')

