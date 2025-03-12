'''
https://leetcode.com/problems/symmetric-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:
            left_node, right_node = stack.pop()
            
            if left_node is None and right_node is None:
                continue

            if left_node is None or right_node is None:
                return False

            if left_node.val == right_node.val:
                stack.append((left_node.left, right_node.right))
                stack.append((left_node.right, right_node.left))
            else:
                return False

        return True
        

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    test1 = sol.isSymmetric(test1_tree)
    print(test1, True)
    assert test1 == True

    test2_tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    test2 = sol.isSymmetric(test2_tree)
    print(test2, False)
    assert test2 == False
    