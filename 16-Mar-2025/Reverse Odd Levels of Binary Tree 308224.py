# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(l, r, level):
            if not l:
                return
            if not level % 2:
                r.val, l.val = l.val, r.val
            dfs(l.left, r.right, level + 1)
            dfs(l.right, r.left, level + 1)
        dfs(root.left, root.right, 0)
        return root 
            
    

    