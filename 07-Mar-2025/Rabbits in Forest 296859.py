# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        c = Counter(answers)
        for i in c:
            if c[i] % (i+1):
                ans += ((c[i] // (i+1))+ 1) * (i+1)
            else:
                ans += (c[i] // (i+1))*(i+1)
        return ans