from math import factorial

n, k = list(map(int, input().split()))
print(factorial(n + k - 1) // (factorial(k) * factorial(n - 1)))
