def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    """
    Time:  O(n * m)
    Space: O(n)
    """
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    n, m, k = len(a), len(a[0]), len(b)

    if m != k:
        return -1

    c = [0] * n
    for row in range(n):
        for col in range(m):
            c[row] += a[row][col] * b[col]

    return c
