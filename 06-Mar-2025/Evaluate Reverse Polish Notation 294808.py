# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = ["+","-","/", "*"]
        for i in range(len(tokens)):
            if tokens[i] not in operations :
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x + y)
                if tokens[i] == "*":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x * y)

                if tokens[i] == "-":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)

                if tokens[i] == "/":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y/x))
        return stack[0]