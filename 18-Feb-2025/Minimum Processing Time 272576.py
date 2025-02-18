# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        n = len(tasks)
        res= 0
        ind = 0 
        ans = 0
        for w in range(n):
            tasks[w] += processorTime[ind]
            res = max(res, tasks[w])
            if not (w+1)%(n//len(processorTime)):
                ind += 1
                ans = max(res, ans)
                res = 0
        return ans