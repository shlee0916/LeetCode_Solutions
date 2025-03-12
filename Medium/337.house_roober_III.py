'''
https://leetcode.com/problems/house-robber-iii/description/
'''

from functools import cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        rob_root = root.val
        not_rob_root = self.rob(root.left) + self.rob(root.right)

        if root.left:
            rob_root += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob_root += self.rob(root.right.left) + self.rob(root.right.right)

        return max(rob_root, not_rob_root)


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    test1 = sol.rob(test1_tree)
    print(test1, 7)
    assert test1 == 7

    test2_tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    test2 = sol.rob(test2_tree)
    print(test2, 9)
    assert test2 == 9
    