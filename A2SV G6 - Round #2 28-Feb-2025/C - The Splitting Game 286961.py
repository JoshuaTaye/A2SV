# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

n = int(input())
lst = []
for j in range(n):
    x = int(input())
    y = input()
    lst.append(y)
for i in lst:
    hm = {}
    for j in i:
        if j not in hm:
            hm[j] = 1
        else:
            hm[j] += 1
    sett = set()
    maxx = 0
    for k in range(len(i)):
        sett.add(i[k])
        if hm[i[k]] > 1:
            hm[i[k]] -= 1
        else:
            del hm[i[k]]
        maxx = max(maxx, len(hm) + len(sett))
    print(maxx)