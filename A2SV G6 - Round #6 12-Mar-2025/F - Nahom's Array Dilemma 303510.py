# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

from collections import deque

def s(arr):
    nn = len(arr)
    prefix = [0] * (nn + 1)
    st = []
    for right, val in enumerate(arr):
        prefix[right] += prefix[right - 1] + val
        while st and arr[st[-1]] <= val:
            left = st.pop()
            if prefix[right] - prefix[left-1] > val:
                return False
        st.append(right)
    return True


tot = int(input())
for l in range(tot):
    n = int(input())
    ar = list(map(int, input().split()))
    if s(ar) and s(ar[::-1]):
        print("YES")
    else:
        print("NO")



