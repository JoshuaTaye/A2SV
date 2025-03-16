# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = []
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        j = self.preOrder(p)
        self.pre = []
        return j == self.preOrder(q)
    def preOrder(self, root):
        if root == None:
            return
        self.preOrder(root.right)
        if not root.left and not root.right:
            self.pre.append((root.val, None, None)) 
        elif not root.left:
            self.pre.append((root.val, None, root.right.val))
        elif not root.right: 
            self.pre.append((root.val, root.left.val, None)) 
        else:
            self.pre.append((root.val, root.left.val, root.right.val))
        self.preOrder(root.left)
        return self.pre
    