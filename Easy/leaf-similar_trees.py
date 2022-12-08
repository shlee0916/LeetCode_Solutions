'''
https://leetcode.com/problems/leaf-similar-trees/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_vals(root: Optional[TreeNode]) -> List[int]:
            stack = [root]
            leaf_vals = []
            while stack:
                cur_node = stack.pop()

                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)

                if not cur_node.left and not cur_node.right:
                    leaf_vals.append(cur_node.val)

            return leaf_vals


        if not root1 or not root2:
            return False

        return get_leaf_vals(root1) == get_leaf_vals(root2)


if __name__ == "__main__":
    sol = Solution()

    test1_tree1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    test1_tree2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    test1 = sol.leafSimilar(test1_tree1, test1_tree2)
    print(test1, True)
    assert test1 == True

    test2_tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    test2_tree2 = TreeNode(1, TreeNode(3), TreeNode(2))
    test2 = sol.leafSimilar(test2_tree1, test2_tree2)
    print(test2, False)
    assert test2 == False
    