'''
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return [-1 ,-1, -1]

            left = dfs(node.left)
            right = dfs(node.right)

            return [left[1] + 1, right[0] + 1,
                max(left[1] + 1, right[0] + 1, left[2], right[2])]

        return dfs(root)[-1]
        

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
    test1 = sol.longestZigZag(test1_tree)
    assert test1 == 3

    test2_tree = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
    test2 = sol.longestZigZag(test2_tree)
    assert test2 == 4

    test3_tree = TreeNode(1)
    test3 = sol.longestZigZag(test3_tree)
    assert test3 == 0
    