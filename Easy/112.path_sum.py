'''
https://leetcode.com/problems/path-sum/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return targetSum - root.val == 0
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    

if __name__ == "__main__":
    sol = Solution()
    
    test_tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7, TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))))
    
    print(sol.hasPathSum(test_tree, 22))