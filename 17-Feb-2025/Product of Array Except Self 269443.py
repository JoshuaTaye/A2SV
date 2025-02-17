# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = [1]
        psi = [1]
        n = len(nums)
        res = []
        for j in range(n):
            ps.append(ps[j] * nums[j])
            psi.append(psi[j] * nums[n-j-1])
        for i in range(n):
            res.append(ps[i]*psi[n-i-1])
        return res
