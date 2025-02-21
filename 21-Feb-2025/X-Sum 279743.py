# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def xSum(ques, row, col):
    maxx = 0
    for i in range(row):
        for j in range(col):
            adds = ques[i][j]
            k = i
            z = j
            adds+=tl(ques,k, z, row, col)
            k = i
            z = j
            adds+=tr(ques, k, z, row, col)
            k = i
            z = j
            adds+=bl(ques, k, z, row, col)
            k = i
            z = j
            adds+=br(ques, k, z, row, col)
            maxx = max(maxx, adds)
    return maxx
def tl(ques, n, m, row, col):
    summ = 0
    n-=1
    m-=1
    while n >= 0 and m >= 0:
        summ+=ques[n][m]
        n-=1
        m-=1
    return summ
def tr(ques, n, m, row, col):
    summ = 0
    n-=1
    m+=1
    while n >= 0 and m < col:
        summ+=ques[n][m]
        n-=1
        m+=1
    return summ
def bl(ques, n, m, row, col):
    summ = 0
    n+=1
    m-=1
    while n < row and m >= 0:
        summ+=ques[n][m]
        n+=1
        m-=1
    return summ
def br(ques, n, m, row, col):
    summ = 0
    n+=1
    m+=1
    while n < row and m < col:
        summ+=ques[n][m]
        n+=1
        m+=1
    return summ

n = int(input())
for i in range(n):
    array = list(map(int, input().split()))
    ques = []
    for i in range(array[0]):
        arr = list(map(int, input().split()))
        ques.append(arr)
    print(xSum(ques, array[0], array[1]))