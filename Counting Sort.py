import math
import os
import random
import re
import sys
def countingSort(arr):
    k=1
    lst=[(0)]*10
    for i in arr:
        lst[i]=lst[i]+1
    print(*lst)
    for i in arr:
        if lst[i-1]>=1:
            lst[i-1]=lst[i-1]+1
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
countingSort(arr)