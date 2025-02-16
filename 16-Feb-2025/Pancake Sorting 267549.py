# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for r in range(n-1, -1, -1):
            maxInd = r
            for i in range(r-1, -1, -1):
                if arr[i] > arr[maxInd]:
                    maxInd = i
            if maxInd != r:
                arr = list(reversed(arr[:maxInd+1])) + arr[maxInd+1:]
                res.append(maxInd+1)
                arr = list(reversed(arr[:r+1])) + arr[r+1:]
                res.append(r+1)
        return res