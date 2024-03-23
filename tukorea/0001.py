def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
  
def reverse(n):
    return int(str(n)[::-1])
  
def isPalindrome(n):
    return reverse(n) == n

N = int(input())
while True:
    if isPalindrome(N) and isPrime(N):
        print(N)
        break
    N += 1