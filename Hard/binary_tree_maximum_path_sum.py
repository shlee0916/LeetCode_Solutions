'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if node is None:
                return 0

            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)

            cur_max = node.val + left_val + right_val
            ans = max(cur_max, ans)

            return node.val + max(left_val, right_val)

        dfs(root)
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    test1 = sol.maxPathSum(test1_tree)
    assert test1 == 6
    
    test2_tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    test2 = sol.maxPathSum(test2_tree)
    assert test2 == 42
    