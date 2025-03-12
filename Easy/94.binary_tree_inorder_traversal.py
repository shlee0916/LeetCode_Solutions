'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            else:
                if stack:
                    node = stack.pop()
                    result.append(node.val)
                
        return result
    

if __name__ == "__main__":
    sol = Solution()
    
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    
    print(sol.inorderTraversal(tree), [1, 3, 2])