from math import factorial

n, k = list(map(int, input().split()))
if k > n:
    print(0)
else:
    print(factorial(n) // (factorial(k) * factorial(n - k)))
