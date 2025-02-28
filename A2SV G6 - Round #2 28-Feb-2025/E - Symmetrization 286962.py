# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

def rotate(mat):
    r = []
    for row in range(len(mat)):
        r.append([])
        for col in range(len(mat[0])):
            r[row].append(mat[col][row])
    for k in range(len(mat)):
        r[k] = r[k][::-1]
    return r
lst = []
n = int(input())
for i in range(n):
    agg = []
    b = int(input())
    for i in range(b):
        y = list(input())
        agg.append(y)
    lst.append(agg)
for entry in lst:
    mat90 = rotate(entry)
    mat180 = rotate(mat90)
    mat270 = rotate(mat180)
    finalRes = 0
    for row in range(len(entry)):
        for col in range(len(entry[0])):
            count = 0
            if entry[row][col] == "0":
                count += 1
            if mat90[row][col] == "0":
                count += 1
            if mat180[row][col] == "0":
                count += 1
            if mat270[row][col] == "0":
                count += 1
            if count == 1 or count == 3:
                finalRes += 1
            elif count == 2:
                finalRes += 2
    print(finalRes//4)






#         if not (len(entry) %2):
#             for i in range(len(entry)):
#                 print(entry[i])
#             print()
#         else:
#             mid = (len(entry) + 1 )//2
#             print(mid)
#             rowDiff = int(entry[mid][:mid]) - int(entry[mid][mid:])
#             print(rowDiff)
