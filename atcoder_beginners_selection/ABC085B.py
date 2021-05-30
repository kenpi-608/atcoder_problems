if __name__ == '__main__':
    N = int(input())
    mochis = [int(input()) for i in range(N)]
    mochis_sorted = sorted(mochis, reverse=True)

    current_mochi = float('inf')
    ans = 0
    for mochi in mochis_sorted:
        if current_mochi > mochi:
            current_mochi = mochi
            ans += 1
    print(ans)
