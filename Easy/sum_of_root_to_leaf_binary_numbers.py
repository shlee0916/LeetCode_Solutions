'''
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 0
        stack = [(root, "")]
        while stack:
            cur_node, cur_val = stack.pop()
            if cur_node.left is None and cur_node.right is None:
                res += int(cur_val + str(cur_node.val), 2)
            
            if cur_node.left:
                stack.append((cur_node.left, cur_val + str(cur_node.val)))
            if cur_node.right:
                stack.append((cur_node.right, cur_val + str(cur_node.val)))
        
        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))
    test1 = sol.sumRootToLeaf(test1_tree)
    assert test1 == 22
    
    test2_tree = TreeNode(0)
    test2 = sol.sumRootToLeaf(test2_tree)
    assert test2 == 0
    