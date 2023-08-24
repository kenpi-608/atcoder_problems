N = int(input())

bet_nums = []
for i in range(N):
    c = int(input())
    bet_nums.append(set(map(int, input().split())))
X = int(input())

candidate_ids = []
candidate_len = []
for j in range(len(bet_nums)):
    if X in bet_nums[j]:
        candidate_ids.append(j+1)
        candidate_len.append(len(bet_nums[j]))

if candidate_len:
    min_len = min(candidate_len)
    anss = []
    for k in range(len(candidate_len)):
        if min_len == candidate_len[k]:
            anss.append(candidate_ids[k])
    print(len(anss))
    print(*sorted(anss))
else:
    print(0)
