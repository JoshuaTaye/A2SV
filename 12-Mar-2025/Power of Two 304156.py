# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

import sys
sys.setrecursionlimit(10**9)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 2:
            return False
        else:
            return self.isPowerOfTwo(n/2)