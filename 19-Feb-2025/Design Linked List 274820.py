# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        node = None
        self.node = node
        
    def get(self, index: int) -> int:
        curr = self.node
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        if curr and count == index:
            return curr.val
        return -1


    def addAtHead(self, val: int) -> None:
        v = Node(val,None)
        v.next = self.node
        self.node = v
 

    def addAtTail(self, val: int) -> None:
        v = Node(val, None)
        if not self.node:
            self.node = v
            return

        curr = self.node
        while curr.next:
            curr = curr.next
        curr.next = v
        


    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(0, self.node)
        v = Node(val, None)
        curr = dummy
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        
        if curr:
            v.next = curr.next
            curr.next = v

        self.node = dummy.next

        
    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0, self.node)
        curr = dummy
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        if curr and curr.next:
            curr.next = curr.next.next
        self.node = dummy.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)