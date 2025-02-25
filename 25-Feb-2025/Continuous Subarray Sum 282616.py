# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if (sums % k) not in remainders:
                remainders[sums%k] = i
            elif i - remainders[sums % k] >= 2:
                return True
        return False