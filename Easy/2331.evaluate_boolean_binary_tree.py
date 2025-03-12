'''
https://leetcode.com/problems/evaluate-boolean-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode) -> bool:
            if node.left is None and node.right is None:
                return True if node.val == 1 else False

            l_val = dfs(node.left)
            r_val = dfs(node.right)

            if node.val == 2:
                return l_val or r_val
            elif node.val == 3:
                return l_val and r_val

        return dfs(root)


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
    test1 = sol.evaluateTree(test1_tree)
    assert test1 == True
    
    test2_tree = TreeNode(0)
    test2 = sol.evaluateTree(test2_tree)
    assert test2 == False
    