# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
[n, limit] = list(map(int, input().split()))
nums = list(map(int, input().split()))
minn = deque()
maxx = deque()
max_len = 0
left = 0
ans = 0
for right in range(n):
    while minn and nums[right] < minn[-1]:
        minn.pop()
    minn.append(nums[right])
    while maxx and nums[right] > maxx[-1]:
        maxx.pop()
    maxx.append(nums[right])

    while maxx and minn and maxx[0] - minn[0] > limit:
        # print(nums[left], nums[right])
        if maxx and maxx[0] == nums[left]:
            maxx.popleft()
        if minn and minn[0] == nums[left]:
            minn.popleft()
        left += 1
    ans += right - left + 1
    max_len = max(right - left + 1, max_len)
# print(ans)
print(ans)

