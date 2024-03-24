def toDecimal(base, number_list):
    result = 0
    nums = number_list[::-1]
    for i in range(len(nums)):
        result += nums[i] * (base**i)
    return result

def decimalToBaseList(base, number):
    result = []
    while number >= base:
        result.insert(0, number % base)
        number //= base
    result.insert(0, number)
    return result

b, N, M = tuple(map(int, input().split()))

n = list(map(int, input().split()))
m = list(map(int, input().split()))

mul = toDecimal(b, n) * toDecimal(b, m)
result = decimalToBaseList(b, mul)
print(len(result))
for n in result:
    print(n, end=' ')