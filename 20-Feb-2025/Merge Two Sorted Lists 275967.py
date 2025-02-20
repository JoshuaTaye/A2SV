# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 
        if not list1:
            return list2
        elif not list2:
            return list1
        p1 = list1
        p2 = list2
        merged = ListNode()
        mp = merged
        while p1 and p2:
            if p1.val <= p2.val:
                mp.next = ListNode(p1.val)
                p1 = p1.next
            else:
                mp.next = ListNode(p2.val)
                p2 = p2.next
            mp = mp.next
        k = merged
        while p1:
            mp.next = ListNode(p1.val)
            p1 = p1.next
            mp = mp.next
        while p2:
            mp.next = ListNode(p2.val)
            k = merged
            p2 = p2.next
            mp = mp.next
        return merged.next

        