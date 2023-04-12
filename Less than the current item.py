def lessthan(a):
    lst=[0]*len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]>a[j]:
                lst[i]=lst[i]+1
    print(lst)
a = list(map(int, input().rstrip().split()))
lessthan(a)
