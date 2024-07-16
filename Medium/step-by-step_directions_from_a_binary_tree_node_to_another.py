'''
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/?envType=daily-question&envId=2024-07-16
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node):
            if not node or node.val in (startValue, destValue):
                return node

            left = lca(node.left)
            right = lca(node.right)

            return node if left and right else left or right

        root = lca(root)

        path_start = ""
        path_dest = ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()

            if node.val == startValue:
                path_start = path
            
            if node.val == destValue:
                path_dest = path

            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))

        return "U" * len(path_start) + path_dest
        

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
    test1 = sol.getDirections(test1_tree, 3, 6)
    assert test1 == "UURL"

    test2_tree = TreeNode(2, TreeNode(1))
    test2 = sol.getDirections(test2_tree, 2, 1)
    assert test2 == "L"
