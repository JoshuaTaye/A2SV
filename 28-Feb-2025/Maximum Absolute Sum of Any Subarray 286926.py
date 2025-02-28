# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        summ = 0
        maxSumm = float("-inf")
        minSumm = float("inf")
        left = 0
        for r in range(len(nums)):
            summ += nums[r]
            maxSumm = max(maxSumm, summ)
            while summ < 0:
                summ -= nums[left]
                left += 1
        left = 0
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            minSumm = min(minSumm, summ)
            while left < len(nums) and summ > 0:
                summ -= nums[left]
                left += 1
        return max(abs(minSumm), maxSumm)