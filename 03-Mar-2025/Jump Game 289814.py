# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 0
        for i in range(len(nums)):
            if i > x:
                return False
            temp_r = nums[i] + i
            x = max(temp_r, x)
        return True
        # i = 0
        # maxx = 0
        # if len(nums) == 1:
        #     return True
        # while i < len(nums) and i + nums[i] < len(nums):
        #     print("nums[i]",nums[i])
        #     if nums[i] + i == len(nums)-1:
        #         return True
        #     elif nums[i] == 0:
        #         return False
        #     else:
        #         local_max = maxx
        #         max_ind = -1
        #         for j in range(nums[i]+1, 0, -1):
        #             if nums[j] > local_max:
        #                 local_max = nums[j]
        #                 max_ind = j
        #         print(max_ind)
        #         if local_max == 0:
        #             return False
        #         i += max_ind  
        # return True
            