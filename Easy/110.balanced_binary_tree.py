'''
https://leetcode.com/problems/balanced-binary-tree/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.__ans = True

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            if abs(left - right) > 1:
                self.__ans = False

            return max(left, right) + 1

        dfs(root)

        return self.__ans


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    test1 = sol.isBalanced(test1_tree)
    assert test1 == True
    
    test2_tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    test2 = sol.isBalanced(test2_tree)
    assert test2 == False
    