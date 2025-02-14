# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()  
        cur_sum = 0
        i = 0
        n = len(costs)
        while i < n and cur_sum + costs[i] <= coins:
            cur_sum += costs[i]
            i += 1
        return i
