A, B = map(int, input().split())

print("M")
for row in range(A):
    s = []
    for col in range(B):
        s.append(str(col+1+B*row))
    print(' '.join(s))

print("R")
for col in range(B):
    s = []
    for row in range(A-1, -1, -1):
        s.append(str(col+1+B*row))
    print(' '.join(s))

print("L")
for col in range(B-1, -1, -1):
    s = []
    for row in range(A):
        s.append(str(col+1+B*row))
    print(' '.join(s))

print("T")
for col in range(B):
    s = []
    for row in range(A):
        s.append(str(col+1+B*row))
    print(' '.join(s))