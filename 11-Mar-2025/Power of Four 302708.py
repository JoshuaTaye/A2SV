# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        return self.checkpower(n)



    def checkpower(self, n):
        if n == 4.0:
            return True
        elif n < 4.0:
            return False
        else:
            return self.checkpower(n/4)