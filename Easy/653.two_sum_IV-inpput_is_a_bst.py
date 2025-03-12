'''
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return
        
        all_val = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
                
            tar = k - cur_node.val
            if tar in all_val:
                return True
            all_val.append(cur_node.val)
                
        return False
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test_tree1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    
    print(sol.findTarget(test_tree1, 9), True)