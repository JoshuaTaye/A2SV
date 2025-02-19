# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        if not head:
            return
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return

        slow = head
        while fast and slow and fast != slow:
            fast = fast.next
            slow = slow.next 
        return slow               

