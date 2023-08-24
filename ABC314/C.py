from collections import defaultdict

N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

same_colors_id = defaultdict(list)
for n in range(N):
    same_colors_id[C[n]].append(n)

ans = ["0"] * len(S)
for m in range(1, M+1):
    k = len(same_colors_id[m])
    for i in range(k):
        ans[same_colors_id[m][(i+1) % k]] = S[same_colors_id[m][i]]

print(''.join(ans))
