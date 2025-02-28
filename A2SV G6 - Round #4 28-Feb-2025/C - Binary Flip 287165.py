# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

def flip(n, a, b):
    summ = 0
    for j in a:
        if j == "1":
            summ += 1
    r = n - 1
    flips = 0
    while r >= 0:
        if not flips % 2:
            if a[r] != b[r] and summ * 2 != r+1:
                return "NO"
            elif a[r] != b[r]:
                flips += 1
                if flips % 2:
                    while r >= 0 and a[r] != b[r]:
                        if a[r] == "1":
                            summ -= 1
                        r -= 1
                else:
                    while r >= 0 and a[r] == b[r]:
                        if a[r] == "1":
                            summ -= 1
                        r -= 1
            else:
                if a[r] == "1":
                    summ -= 1
                r -= 1
        else:
            if a[r] == b[r] and summ * 2 != r+1:
                return "NO"
            elif a[r] == b[r]:
                flips += 1
                if flips % 2:
                    while r >= 0 and a[r] != b[r]:
                        if a[r] == "1":
                            summ -= 1
                        r -= 1
                else:
                    while r >= 0 and a[r] == b[r]:
                        if a[r] == "1":
                            summ -= 1
                        r -= 1
            else:
                if a[r] == "1":
                    summ -= 1
                r -= 1
    return "YES"




total = int(input())
for i in range(total):
    n = int(input())
    a = input()
    b = input()
    print(flip(n, a, b))


