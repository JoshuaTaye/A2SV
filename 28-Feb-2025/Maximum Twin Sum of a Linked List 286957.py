# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        j = head
        summ = 0
        curr.prev = None
        while curr.next:
            curr.next.prev = curr
            curr = curr.next
        while j:
            summ = max(summ, j.val + curr.val)
            j = j.next
            curr = curr.prev
        return summ
