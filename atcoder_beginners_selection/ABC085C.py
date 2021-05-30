def check_really(N, Y):
    for x in range(N + 1):
        for y in range(N - x + 1):
            if 10000 * x + 5000 * y + 1000 * (N - x - y) == Y:
                return x, y, N - x - y
    return -1, -1, -1


N, Y = map(int, input().split())

x, y, z = check_really(N, Y)
print(x, y, z)