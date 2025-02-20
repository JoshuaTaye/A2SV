# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        count = 0
        d = ListNode(0, head)
        curr = d
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return d.next

        