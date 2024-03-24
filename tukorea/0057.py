def nextPermutation(arr: list):
    for i in range(len(arr)-1, 0, -1):
        if arr[i-1] < arr[i]:
            break
        
    pin = arr[i-1]
    m = arr[i]
    idx = i
    for j in range(i, len(arr)):
        if pin < arr[j] <= m:
            m = arr[j]
            idx = j
    
    arr[i-1], arr[idx] = arr[idx], arr[i-1]
    arr[i:] = sorted(arr[i:])
    
    return arr


(N, K) = tuple(map(int, input().split()))

for _ in range(K):
    p = list(map(int, input().split()))
    for n in nextPermutation(p):
        print(n, end=' ')
    print()
