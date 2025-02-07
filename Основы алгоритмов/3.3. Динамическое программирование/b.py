n, m = list(map(int, input().split()))
R = [[None] * (m + 1) for _ in range(n + 1)]
R[0][0] = False

# fill first 2 columns
for i in range(1, n + 1):
    R[i][0] = True if i % 3 else False
    R[i][1] = True if (i - 1) % 3 else False

# fill first 2 rows
for j in range(1, m + 1):
    R[0][j] = True if j % 3 else False
    R[1][j] = True if (j - 1) % 3 else False

for i in range(2, n + 1):
    for j in range(2, m + 1):
        # if all these fields are win, you definetely lose
        if (
            R[i - 1][j]
            and R[i][j - 1]
            and R[i - 2][j]
            and R[i][j - 2]
            and R[i - 1][j - 2]
            and R[i - 2][j - 1]
        ):
            R[i][j] = False
        else:
            R[i][j] = True


if R[n][m]:
    print("Win")
else:
    print("Lose")

#################
# MATH SOLUTION #
#################
# n, m = list(map(int, input().split()))
# if n % 3 == m % 3:
#     print("Lose")
# else:
#     print("Win")
