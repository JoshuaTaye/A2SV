# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = float("-inf")
        s = 0
        left = 0
        for r in range(len(nums)):
            s += nums[r]
            ms = max(ms, s)
            while s < 0:
                s -= nums[left]
                left += 1
        return ms