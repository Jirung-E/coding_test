TESTCASE = int(input())

for _ in range(TESTCASE):
    N = int(input())
    curr = input()
    goal = input()

    to_W = 0
    to_B = 0

    for i in range(N):
        if curr[i] != goal[i]:
            if goal[i] == 'W':
                to_W += 1
            else:
                to_B += 1

    print(max(to_W, to_B))
 