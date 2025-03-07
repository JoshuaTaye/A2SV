# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.left = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.left += 1
        return self.stack[self.left-1]

    def peek(self) -> int:
        return self.stack[self.left]

    def empty(self) -> bool:
        return len(self.stack) == self.left
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()