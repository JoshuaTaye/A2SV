# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps = [0,nums[0]]
        n = len(nums)
        for j in range(1, n):
            ps.append(ps[j] + nums[j])
        res = 0
        hm = {}
        for i in range(n+1):
            x = ps[i]%k
            if x in hm:
                res += hm[x]
                hm[x] += 1
            else:
                hm[x] = 1
        return res