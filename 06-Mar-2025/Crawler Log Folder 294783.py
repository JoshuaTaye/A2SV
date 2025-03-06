# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in logs:
            if i[1] == ".":
                if res > 0:
                    res -= 1
            elif i[0] != ".":
                res += 1
        return res