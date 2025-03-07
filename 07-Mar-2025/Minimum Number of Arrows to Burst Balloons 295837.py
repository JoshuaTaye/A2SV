# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res = 1
        left = 0
        n = len(points)
        for i in range(n):
            if points[i][0] > points[left][1]:
                left = i
                res += i - left + 1
        return res