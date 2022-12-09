'''
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root, max_val, min_val):
            if root:
                self.ans = max(self.ans, max_val - root.val, root.val - min_val)
                new_max = max(root.val, max_val)
                new_min = min(root.val, min_val)

                dfs(root.left, new_max, new_min)
                dfs(root.right, new_max, new_min)

        dfs(root, root.val, root.val)

        return self.ans


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
    test1 = sol.maxAncestorDiff(test1_tree)
    print(test1, 7)
    assert test1 == 7

    test2_tree = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
    test2 = sol.maxAncestorDiff(test2_tree)
    print(test2, 3)
    assert test2 == 3
