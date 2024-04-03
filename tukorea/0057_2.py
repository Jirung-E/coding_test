# import itertools

# print(list(itertools.permutations([1, 2, 3, 4]))) 

def nextPermutation(arr: list):
    for i in range(len(arr)-1, 0, -1):
        if arr[i-1] < arr[i]:
            R = arr[i-1:]
            R.sort()
            j = R.index(arr[i-1])
            number = R.pop(j+1)
            R.insert(0, number)
            arr = arr[:i-1] + R
            return arr


(N, K) = tuple(map(int, input().split()))

for _ in range(K):
    p = list(map(int, input().split()))
    for n in nextPermutation(p):
        print(n, end=' ')
    print()
