# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage, None)
        self.tail = ListNode(0)
        self.tail.prev = self.head
        self.curr = self.tail.prev

    def visit(self, url: str) -> None:
        self.insertAtTail(url)

    def back(self, steps: int) -> str:
        j = steps

        while j > 0 and self.curr.prev:
            self.curr = self.curr.prev
            j -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        j = steps
        while j > 0 and self.curr.next:
            self.curr = self.curr.next
            j -= 1
        return self.curr.val

    def insertAtTail(self, item) -> None:
        v = ListNode(item, None)
        self.curr.next = v
        v.prev = self.curr
        self.curr = self.curr.next


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)