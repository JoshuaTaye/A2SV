def insertionSort1(n, arr):
    a=arr[-1]
    k=0
    for i in range(n):
        if a<=arr[n-2-i] and i<=n-2:
            arr[n-1-i]=arr[n-2-i]
            print(*arr)
        if a>arr[n-1-i] and k<1:
            k=k+1
            arr[n-i]=a
            print(*arr)
    if a<arr[0]:
        arr[0]=a
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
insertionSort1(n, arr)