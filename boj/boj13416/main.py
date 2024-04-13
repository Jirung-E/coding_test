TESTCASE = int(input())

for _ in range(TESTCASE):
    N = int(input())
    result = 0
    for day in range(N):
        stocks = map(int, input().split())
        result += max(*stocks, 0)
    print(result)