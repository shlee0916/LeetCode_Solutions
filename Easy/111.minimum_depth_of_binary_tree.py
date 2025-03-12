'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left and root.right:
            return min(left, right) + 1

        return max(left, right) + 1


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    test1 = sol.minDepth(test1_tree)
    assert test1 == 2

    test2_tree = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    test2 = sol.minDepth(test2_tree)
    assert test2 == 5
    