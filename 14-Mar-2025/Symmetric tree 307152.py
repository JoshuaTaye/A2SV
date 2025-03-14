# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = []
        self.post = []
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        curr1 = root
        curr2 = root
        return self.postOrder(curr1) == self.preOrder(curr1)
    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        if not root.left and not root.right:
            self.post.append((root.val, None, None)) 
        elif not root.left:
            self.post.append((root.val, root.right.val, None))
        elif not root.right: 
            self.post.append((root.val, None, root.left.val)) 
        else:
            self.post.append((root.val, root.right.val, root.left.val))
        self.postOrder(root.right)
        return self.post
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
        