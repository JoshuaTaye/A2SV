# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s =  sorted(list(s), reverse=True)
        if s[-1] == "1":
            return "".join(s)
        for i in range(len(s)-2, -1, -1):
            if s[i] == "1":
                s[i] = "0"
                s[-1] = "1"
                break
        return "".join(s)