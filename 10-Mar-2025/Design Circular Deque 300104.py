# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxx = k
        self.deq = []
        self.len = 0

    def insertFront(self, value: int) -> bool:
        if self.len == self.maxx:
            return False
        self.deq.insert(0, value)
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.maxx:
            return False
        self.deq.append(value)
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.deq = self.deq[1:]
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.deq.pop()
        self.len -= 1
        return True
        

    def getFront(self) -> int:
        if self.len == 0:
            return -1
        return self.deq[0]

    def getRear(self) -> int:
        if self.len == 0:
            return -1
        return self.deq[-1]

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.maxx
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()