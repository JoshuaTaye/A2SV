# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
        def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
            summ = 0
            count = 0
            hm = defaultdict(int)
            hm[0] = 1
            for r in range(len(nums)):
                summ += nums[r]
                if summ - goal in hm:
                    count += hm[summ-goal]
                hm[summ] += 1
            return count