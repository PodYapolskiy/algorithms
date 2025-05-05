def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Time:  O(n * m)
    Space: O(n * m)
    """
    n, m = len(a), len(a[0])
    b = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]

    return b
