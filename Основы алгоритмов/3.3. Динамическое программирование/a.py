n, m = list(map(int, input().split()))
R = {(0, 0): False}  # rewards

# base case when stowns are only in 1 group
for i in range(1, n + 1):
    R[(i, 0)] = not R[(i - 1, 0)]

# similar but for other group
for i in range(1, m + 1):
    R[(0, i)] = not R[(0, i - 1)]

# iterate through all n * m cases
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # lose if all 3 upper corner for current are win positions
        if R[(i - 1, j - 1)] and R[(i, j - 1)] and R[(i - 1, j)]:
            R[(i, j)] = False
        else:
            R[(i, j)] = True

if R[(n, m)]:
    print("Win")
else:
    print("Lose")
