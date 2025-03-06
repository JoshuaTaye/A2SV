# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        hm = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                number = s.pop()
                hm[number] = i - number
            s.append(i)
        return hm