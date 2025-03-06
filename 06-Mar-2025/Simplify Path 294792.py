# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, x: str) -> str:
        stack = deque()
        path = x.split("/")
        absolute = "/"
        for i in range(len(path)):
            if path[i] == "..":
                if stack and stack[-1] != "/":
                    stack.pop()
            elif path[i] != "" and path[i] != ".":
                stack.append(path[i])
        print(stack)
        for i in range(len(stack)):
            absolute += stack[i] + "/"
        if len(absolute) > 1:
            absolute = absolute[:-1]
        return absolute