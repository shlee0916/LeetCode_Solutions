'''
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
'''

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traversal(root: TreeNode) -> List[int]:
            res = []
            if root:
                stack = [root]
                while stack:
                    cur_node = stack.pop()
                    res.append(cur_node.val)

                    if cur_node.left:
                        stack.append(cur_node.left)
                    if cur_node.right:
                        stack.append(cur_node.right)

            return res

        result = []
        result.extend(traversal(root1))
        result.extend(traversal(root2))

        return sorted(result)


if __name__ == "__main__":
    sol = Solution()

    test1_tree1 = TreeNode(2, TreeNode(1), TreeNode(4))
    test1_tree2 = TreeNode(1, TreeNode(0), TreeNode(3))
    test1 = sol.getAllElements(test1_tree1, test1_tree2)
    print(test1)
    assert test1 == [0, 1, 1, 2, 3, 4]

    test2_tree1 = TreeNode(1, None, TreeNode(8))
    test2_tree2 = TreeNode(8, TreeNode(1))
    test2 = sol.getAllElements(test2_tree1, test2_tree2)
    print(test2)
    assert test2 == [1, 1, 8, 8]
    