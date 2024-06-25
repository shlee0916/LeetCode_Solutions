'''
https://leetcode.com/problems/flip-equivalent-binary-trees/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1 = [root1]
        stack2 = [root2]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 == node2 == None:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            if (node1.left == node2.left == None or
                node1.left and node2.left and
                node1.left.val == node2.left.val):
                stack1.extend([node1.left, node1.right])
            else:
                stack1.extend([node1.right, node1.left])
            stack2.extend([node2.left, node2.right])

        return not stack1 and not stack2


if __name__ == "__main__":
    sol = Solution()

    test1_tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
    test2_tree2 = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
    test1 = sol.flipEquiv(test1_tree1, test2_tree2)
    assert test1 == True

    test2_tree1 = TreeNode()
    test2_tree2 = TreeNode()
    test2 = sol.flipEquiv(test2_tree1, test2_tree2)
    assert test2 == True

    test3_tree1 = TreeNode()
    test3_tree2 = TreeNode(1)
    test3 = sol.flipEquiv(test3_tree1, test3_tree2)
    assert test3 == False
