# コード
n = input()
a = list(map(int, input().split()))
ans = float('inf')
for i in a:
  ans = min(ans, len(bin(i)) - bin(i).rfind('1') - 1)
print(ans)