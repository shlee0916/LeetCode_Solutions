'''
https://leetcode.com/problems/validate-binary-search-tree/description/
'''

from tkinter.tix import Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val >= root.val:
                return False
            
            prev = root
            root = root.right
            
        return True
    

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    root2 = TreeNode(5,
                     TreeNode(1),
                     TreeNode(4, TreeNode(3), TreeNode(6)))
    
    
    print(sol.isValidBST(root1))
    print(sol.isValidBST(root2))