n = int(input())
line = input()

M = []
M.append(['.'] * n)
r = 0
p = '.'

for c in range(n):
    if line[c] == '+':
        if p == '/':
            r -= 1
            if r < 0:
                r = 0
                M.insert(0, ['.'] * n)
        M[r][c] = '/'
        p = '/'
    elif line[c] == '-':
        if p == '\\' or p == '_':
            r += 1
            if r >= len(M):
                M.append(['.'] * n)
        M[r][c] = '\\'
        p = '\\'
    else:
        if p == '/':
            r -= 1
            if r < 0:
                r = 0
                M.insert(0, ['.'] * n)
        M[r][c] = '_'
        p = '_'

for row in M:
    for stamp in row:
        print(stamp, end='')
    print()