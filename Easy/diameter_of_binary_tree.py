'''
https://leetcode.com/problems/diameter-of-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.ans = max(self.ans, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)

        return self.ans


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    test1 = sol.diameterOfBinaryTree(test1_tree)
    assert test1 == 3
    
    test2_tree = TreeNode(1, TreeNode(2))
    test2 = sol.diameterOfBinaryTree(test2_tree)
    assert test2 == 1
    