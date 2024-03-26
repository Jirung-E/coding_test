width = int(input())

graph = {0: ['.' for _ in range(width)]}

stamp = {
    '+': '/', 
    '-': '\\',
    '=': '_'
}
flag = None    # -1, 0, 1
y = 0
for i, c in enumerate(input()):
    if c == '+':
        if flag == 1:
            y += 1
        flag = 1
    if c == '-':
        if flag == -1 or flag == 0:
            y -= 1
        flag = -1
    if c == '=':
        if flag == 1:
            y += 1
        flag = 0

    if y not in graph.keys():
        graph[y] = ['.' for _ in range(width)]

    graph[y][i] = stamp[c]


y_max = max(graph.keys())
y_min = min(graph.keys())

for y in range(y_max, y_min-1, -1):
    for c in graph[y]:
        print(c, end='')
    print()