# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        counter=head
        while counter:
            count += 1
            counter = counter.next
        l = count // k
        dummy = ListNode(0, head)
        d = ListNode(0)
        curr = dummy
        beg = d
        p = 0
        for p in range(l):
            for i in range(k):
                if curr and curr.next:
                    self.insertAtBeg(beg, curr.next)
                    curr = curr.next
                else:
                    return d.next
            for j in range(k):
                beg = beg.next
        curr = curr.next
        while curr and beg:
            beg.next = curr
            beg = beg.next
            curr = curr.next
        return d.next

    def insertAtBeg(self, start, node) -> None:
        temp = start.next
        p = ListNode(node.val, None)
        start.next = p
        p.next = temp



