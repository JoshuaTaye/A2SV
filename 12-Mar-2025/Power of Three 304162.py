# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

import sys
sys.setrecursionlimit(10**9)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3:
            return False
        return self.isPowerOfThree(n/3)