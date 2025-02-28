# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
lst = list(map(int, input().split()))
ss  = [lst[-1]]
ps = [lst[0]]

prevd = [0]
lst.sort()
minim = [0]
maxim = [0]
for i in range(1, len(lst)):
   minim.append(minim[i-1] + lst[i] - lst[i-1])
for i in range(1, len(minim)):
    minim[i] = minim[i-1] + minim[i]
maxim = list(reversed(minim))
minn = float("inf")
minind = -1

for p in range(len(minim)):
    if minim[p] + maxim[p] < minn:
        minind = p
        minn = minim[p] + maxim[p]
print(lst[minind])


# for j in range(len(lst)):
#     d =


# distancea = ps[]


# ss = list(reversed(ss))
# print(ss)
# print(ps)