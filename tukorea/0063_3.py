row, col = map(int, input().split())

print("M")
for r in range(row):
    for c in range(col):
        if c < col-1:
            print(col*r+c+1, end=' ')
        else:
            print(col*r+c+1)

print("R")
for c in range(col):
    for r in range(row-1, -1, -1):
        if r > 0:
            print(col*r+c+1, end=' ')
        else:
            print(col*r+c+1)

print("L")
for c in range(col-1, -1, -1):
    for r in range(row):
        if r < row-1:
            print(col*r+c+1, end=' ')
        else:
            print(col*r+c+1)

print("T")
for c in range(col):
    for r in range(row):
        if r < row-1:
            print(col*r+c+1, end=' ')
        else:
            print(col*r+c+1)