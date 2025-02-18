# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1,p2 = 0,0
        res = []
        while p1 < len(firstList) and p2 < len(secondList):
            fs = firstList[p1][0]
            fe = firstList[p1][1]
            ss = secondList[p2][0]
            se = secondList[p2][1]
            if fs <= se and ss <= fe:
                res.append([max(fs, ss), min(fe, se)])
            if fe <= se:
                p1 += 1
            else:
                p2 += 1
        return res
