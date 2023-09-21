'''
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def dfs(node, path):
            ans = 0
            if node is None:
                return 0

            if node.val in path:
                path.remove(node.val)
            else:
                path.add(node.val)

            if node.left is None and node.right is None:
                if len(path) <= 1:
                    ans += 1
            else:
                ans = ans + dfs(node.left, path) + dfs(node.right, path)

            if node.val in path:
                path.remove(node.val)
            else:
                path.add(node.val)

            return ans

        return dfs(root, set())
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
    test1 = sol.pseudoPalindromicPaths(test1_tree)
    assert test1 == 2
    
    test2_tree = TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))
    test2 = sol.pseudoPalindromicPaths(test2_tree)
    assert test2 == 1
    