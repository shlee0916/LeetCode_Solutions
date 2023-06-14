'''
https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            
            values.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        return min(b - a for a, b in zip(values, values[1:]))


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    test1 = sol.getMinimumDifference(test1_tree)
    assert test1 == 1

    test2_tree = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
    test2 = sol.getMinimumDifference(test2_tree)
    assert test2 == 1
