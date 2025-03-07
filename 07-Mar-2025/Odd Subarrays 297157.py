# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

tot = int(input())
for i in range(tot):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    j = 0
    while j < len(lst)-1:
        if lst[j] > lst[j+1]:
            ans += 1
            j += 1
        j += 1
    print(ans)

