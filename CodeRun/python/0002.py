def main():
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    mem = [[0] * m for _ in range(n)]
    mem[0][0] = arr[0][0]

    for i in range(1, n):
        mem[i][0] = mem[i - 1][0] + arr[i][0]

    for j in range(1, m):
        mem[0][j] = mem[0][j - 1] + arr[0][j]

    for i in range(1, n):
        for j in range(1, m):
            # минимальный элемент из верхнего и левого + нынешний
            mem[i][j] = min(mem[i][j - 1], mem[i - 1][j]) + arr[i][j]

    print(mem[n - 1][m - 1])


if __name__ == "__main__":
    main()
