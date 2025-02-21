# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()
        l,m = less,more
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                m.next = head
                m = m.next
            head = head.next
        m.next = None
        more = more.next
        # more = more.next
        while more:
            l.next = ListNode(more.val, None)
            l = l.next
            more = more.next
        return less.next

