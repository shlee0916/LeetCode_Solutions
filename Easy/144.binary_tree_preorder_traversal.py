'''
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result


if __name__ == "__main__":
    sol = Solution()

    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))

    print(sol.preorderTraversal(tree))