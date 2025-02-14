# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

[n, k] = list(map(int, input().split()))
nums = list(map(int, input().split()))
sett = defaultdict(int)
max_len = 0
l = 0
ans = []
for r in range(n):
    sett[nums[r]] += 1
    while len(sett) > k:
        sett[nums[l]] -= 1
        if sett[nums[l]] == 0:
            del sett[nums[l]]
        l += 1
    if r - l + 1 > max_len:
        max_len = r - l + 1
        ans = [l+1 , r+1]
print(*ans)



