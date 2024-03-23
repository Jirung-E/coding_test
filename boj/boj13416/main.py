TESTCASE = int(input())

for _ in range(TESTCASE):
    N = int(input())
    result = 0
    for day in range(N):
        A, B, C = map(int, input().split())
        result += max(A, B, C, 0)
    print(result)