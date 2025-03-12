'''
https://leetcode.com/problems/binary-tree-tilt/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if node is None:
                return 0
            
            left_val = dfs(node.left)
            right_val = dfs(node.right)

            self.ans += abs(left_val - right_val)

            return node.val + left_val + right_val

        dfs(root)

        return self.ans


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    test1 = sol.findTilt(test1_tree)
    assert test1 == 1
    
    test2_tree = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
    test2 = sol.findTilt(test2_tree)
    assert test2 == 15
    
    test3_tree = TreeNode(21, TreeNode(7, TreeNode(1, TreeNode(3), TreeNode(3)), TreeNode(1)), TreeNode(14, TreeNode(2), TreeNode(2)))
    test3 = sol.findTilt(test3_tree)
    assert test3 == 9
    