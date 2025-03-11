# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:

        fact = self.factoria(n)
        zeros = 0
        while not fact % 10:
            fact = fact//10
            zeros += 1
        return zeros
        for i in range(len(fact)-1, -1, -1):
            if fact[i] == "0":
                zeros += 1
            else:
                break
        return zeros

    def factoria(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.factoria(n-1)
