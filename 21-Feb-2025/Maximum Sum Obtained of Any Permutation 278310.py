# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        x = [0]  * (n)

        for i in requests:
            x[i[0]] += 1
            if i[1] < len(nums)-1:
                x[i[1]+1] -= 1
        for o in range(1, len(x)):
            x[o] = x[o-1] + x[o]

        hm = {}
        for i in range(n):
            hm[i] = x[i]
        new_nums = [0]* n
        c = sorted(hm.items(),key = lambda item: item[-1] ,reverse=True)
        nums.sort(reverse=True)

        for t in range(n):
            new_nums[c[t][0]] = nums[t]

        for k in range(1, n):
            new_nums[k] = new_nums[k-1] + new_nums[k]
        res = 0
        for j in requests:
            if j[0] == 0:
                res += new_nums[j[1]]
            else:
                res += (new_nums[j[1]] - (new_nums[j[0] - 1]))
                
        return res% ((10**9) + 7)