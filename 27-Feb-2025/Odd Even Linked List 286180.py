# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddcurr = head
        if not head:
            return
        p = ListNode(0, None)
        new = p
        while oddcurr:
            new.next = ListNode(oddcurr.val, None)
            new = new.next
            if oddcurr.next:
                oddcurr = oddcurr.next.next
            else:
                break
        even_curr = head.next
        while even_curr:
            new.next = ListNode(even_curr.val, None)
            new = new.next
            if even_curr.next:
                even_curr = even_curr.next.next
            else:
                break
        return p.next