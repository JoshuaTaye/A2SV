# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        n= ListNode(0, None)
        new = n
        if left == right:
            return head
        l = 0
        while l < left-1:
            new.next = ListNode(curr.val, None)
            curr = curr.next
            new = new.next
            l += 1
        while l <= right-1:
            temp = new.next
            v = ListNode(curr.val, None)
            new.next = v
            v.next = temp
            curr = curr.next
            l +=1
        for i in range(right - left+1):
            new = new.next
        while curr:
            new.next = ListNode(curr.val, None)
            new = new.next
            curr = curr.next

        return n.next


        # r = l+1
        # while r < right:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        #     r += 1
        # while curr:
        #     curr = curr.next
        # return head