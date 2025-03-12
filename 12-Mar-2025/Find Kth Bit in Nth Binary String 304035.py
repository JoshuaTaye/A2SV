# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(inp):
            p = [str(inp), "1"]
            l = []
            for i in range(len(inp)):
                l.append(str(1-int(inp[i])))
            p.extend(l[::-1])
            return "".join(p)
        if n == 0:
            return "0"
        x = "0"
        for j in range(n):
            x = solve(x)
        return x[k-1]