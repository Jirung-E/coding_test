row, col = map(int, input().split())

def showMatrix(mat):
    for row in mat:
        print(' '.join(row))

print("M")
M = []
for r in range(row):
    R = []
    for c in range(col):
        R.append(str(col*r+c+1))
    M.append(R)
showMatrix(M)

print("R")
R = [[M[r][c] for r in range(row-1, -1, -1)] for c in range(col)]
showMatrix(R)

print("L")
L = [[M[r][c] for r in range(row)] for c in range(col-1, -1, -1)]
showMatrix(L)

print("T")
T = [[M[r][c] for r in range(row)] for c in range(col)]
showMatrix(T)