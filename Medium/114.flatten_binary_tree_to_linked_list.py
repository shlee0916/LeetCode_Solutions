'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            all_values = []

            stack = [root]
            while stack:
                cur_node = stack.pop()

                all_values.append(cur_node)
                if cur_node.right is not None:
                    stack.append(cur_node.right)
                    cur_node.right = None
                if cur_node.left is not None:
                    stack.append(cur_node.left)
                    cur_node.left = None

            all_values = all_values[::-1]
            new_root = all_values.pop()
            while all_values:
                new_root.right = all_values.pop()
                new_root = new_root.right
                
            root = new_root
            
            
if __name__ == "__main__":
    sol = Solution()
    test_node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    
    sol.flatten(test_node)
    while test_node:
        print(test_node.val)
        test_node = test_node.right