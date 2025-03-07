# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        c = 0
        stack = []
        multiplier = 0
        for i in range(len(s)):
            if s[i] == "(":
                multiplier = 1
                stack.append("(")
            elif stack and s[i] == ")":
                stack.pop()
                if multiplier == 1:
                    c += 2 ** (len(stack))
                    multiplier = 0
        return c

