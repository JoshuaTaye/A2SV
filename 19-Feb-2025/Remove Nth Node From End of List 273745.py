# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
        curr = dummy
        while curr:
            curr = curr.next
            count += 1
        curr = dummy
        count2 = 1
        while count2 < count-n:
            curr = curr.next
            count2 += 1
        if curr.next:
            curr.next = curr.next.next
        return dummy.next
            