# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 3:
            return x * x * x
        if n < 0:
            x = 1/x
            n = -1*n
        return self.powee(x, n)


    def powee(self, x, n):
        if n == 1:
            return x
        z = self.powee(x, n//2)
        if n % 2:
            return (z * z * x)
        else:
            return (z * z)