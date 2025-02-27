# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        st2 = []
        cur1= l1
        cur2 = l2
        while cur1:
            st1.append(str(cur1.val))
            cur1 = cur1.next
        while cur2:
            st2.append(str(cur2.val))
            cur2 = cur2.next
        x = int("".join(list(reversed(st1))))
        y = int("".join(list(reversed(st2))))
        rev = list(reversed(list(str(x+y))))
        p = ListNode(int(rev[0]), None)
        j = p 
        for k in range(1, len(rev)):
            j.next = ListNode(int(rev[k]), None)
            j = j.next
        return p

