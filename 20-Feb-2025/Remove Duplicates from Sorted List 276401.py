# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hm = set()
        dummy = ListNode(0, head)
        curr = dummy
        while curr and curr.next:
            if curr.next.val in hm:
                curr.next = curr.next.next
            else:
                hm.add(curr.next.val)
                curr = curr.next
        return dummy.next

