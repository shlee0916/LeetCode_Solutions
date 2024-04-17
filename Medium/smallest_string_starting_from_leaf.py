'''
https://leetcode.com/problems/smallest-string-starting-from-leaf/?envType=daily-question&envId=2024-04-17
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        self.ans = ""
        def dfs(node, string):
            string = string + chr(ord("a") + node.val)

            if node.left is None and node.right is None:
                if self.ans == "":
                    self.ans = string[::-1]
                else:
                    self.ans = min(self.ans, string[::-1])

            if node.left:
                dfs(node.left, string)
            if node.right:
                dfs(node.right, string)

        dfs(root, "")

        return self.ans


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
    test1 = sol.smallestFromLeaf(test1_tree)
    assert test1 == "dba"
    
    test2_tree = TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2)))
    test2 = sol.smallestFromLeaf(test2_tree)
    assert test2 == "adz"
    
    test3_tree = TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode(0))), TreeNode(1, TreeNode(0)))
    test3 = sol.smallestFromLeaf(test3_tree)
    assert test3 == "abc"
    