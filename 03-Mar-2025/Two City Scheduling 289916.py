# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        x = [((a-b), a, b) for [a,b] in costs]
        x.sort()
        cost = 0
        j = 0
        for i in x:
            if j < len(costs)//2:
                cost += i[1]
                j += 1
            else:
                cost += i[2]
                j += 1
        return cost

        
