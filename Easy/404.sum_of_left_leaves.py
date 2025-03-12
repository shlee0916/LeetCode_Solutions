'''
https://leetcode.com/problems/sum-of-left-leaves/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        stack = [root]
        while stack:
            cur_node = stack.pop()
            
            
            if cur_node.right is not None:
                stack.append(cur_node.right)
                
            if cur_node.left is not None:
                if cur_node.left.left is None and cur_node.left.right is None:
                    total += cur_node.left.val
                else:
                    stack.append(cur_node.left)
                
        return total


if __name__ == "__main__":
    sol = Solution()

    test_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    print(sol.sumOfLeftLeaves(test_tree))