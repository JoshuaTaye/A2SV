# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

[n, k] = list(map(int, input().split()))
arr = list(map(int, input().split()))
ps = [0]
for i in range(1, len(arr)):
    ps.append(arr[i] - arr[i-1])
ps.sort()
ans = 0
i = n - (k-1)
for x in range(i):
    ans += ps[x]
print(ans)