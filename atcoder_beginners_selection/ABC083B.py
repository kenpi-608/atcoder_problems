if __name__ == '__main__':
    N, A, B = map(int, input().split())
    ans = 0
    for num in range(1, N + 1):
        digit_sum = sum([int(i) for i in str(num)])
        if A <= digit_sum <= B:
            ans += num
    print(ans)
