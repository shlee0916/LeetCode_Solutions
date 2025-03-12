'''
https://leetcode.com/problems/cousins-in-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False

        def dfs(node, level, parents, target):
            if node:
                if node.val == target:
                    return level + 1, parents

                return dfs(node.left, level + 1, node, target) or dfs(node.right, level + 1, node, target)

        level_x, x_parents = dfs(root, 0, None, x)
        level_y, y_parents = dfs(root, 0, None, y)

        return level_x == level_y and x_parents != y_parents


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    test1 = sol.isCousins(test1_tree, 4, 3)
    assert test1 == False
    
    test2_tree = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    test2 = sol.isCousins(test2_tree, 5, 4)
    assert test2 == True
    
    test3_tree = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    test3 = sol.isCousins(test3_tree, 2, 3)
    assert test3 == False
    