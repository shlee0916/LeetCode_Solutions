'''
https://leetcode.com/problems/maximum-width-of-binary-tree/description/
'''

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return

        que = deque([[0, 0, root]]) # [level, num, node]
        levels = []
        while que:
            cur_level_len = len(que)
            level_nodes = []
            for _ in range(cur_level_len):
                cur_level, num, cur_node = que.popleft()
                level_nodes.append([cur_level, num, cur_node])

                if cur_node.left:
                    que.append([cur_level + 1, num * 2, cur_node.left])
                if cur_node.right:
                    que.append([cur_level + 1, num * 2 + 1, cur_node.right])

            levels.append(level_nodes)

        width_info = [level[-1][1] - level[0][1] + 1 for level in levels if len(level) > 1]

        return max(width_info) if width_info else 1


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    test1 = sol.widthOfBinaryTree(test1_tree)
    assert test1 == 4

    test2_tree = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7))))
    test2 = sol.widthOfBinaryTree(test2_tree)
    assert test2 == 7

    test3_tree = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    test3 = sol.widthOfBinaryTree(test3_tree)
    assert test3 == 2
    