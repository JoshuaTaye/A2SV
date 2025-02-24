# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ps = [0] * n
        ss = [0] * n
        res = [0] * n

        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = ps[i - 1] + nums[i]
        
        ss[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            ss[i] = ss[i + 1] + nums[i]
        
        for i in range(n):
            ls = ps[i - 1] if i > 0 else 0
            rs = ss[i + 1] if i < n - 1 else 0
            res[i] = (i * nums[i] - ls) + (rs - (n - i - 1) * nums[i])
        
        return res