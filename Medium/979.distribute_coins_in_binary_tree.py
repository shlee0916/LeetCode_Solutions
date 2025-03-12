'''
https://leetcode.com/problems/distribute-coins-in-binary-tree/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.__ans = 0
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.__ans += abs(left) + abs(right)

            return node.val + left + right - 1

        dfs(root)

        return self.__ans


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(3, TreeNode(0), TreeNode(0))
    test1 = sol.distributeCoins(test1_tree)
    assert test1 == 2

    test2_tree = TreeNode(0, TreeNode(3), TreeNode(0))
    test2 = sol.distributeCoins(test2_tree)
    assert test2 == 3
    