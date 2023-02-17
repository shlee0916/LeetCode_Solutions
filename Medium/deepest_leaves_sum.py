'''
https://leetcode.com/problems/deepest-leaves-sum/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        res = 0
        que = [root]
        levels = []
        while que:
            cur_level = []
            level_len = len(que)
            for _ in range(level_len):
                cur_node = que.pop(0)
                cur_level.append(cur_node.val)

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

                levels.append(cur_level)

        return sum(levels[-1])


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
    test1 = sol.deepestLeavesSum(test1_tree)
    print(test1, 15)
    assert test1 == 15

    test2_tree = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
    test2 = sol.deepestLeavesSum(test2_tree)
    print(test2, 19)
    assert test2 == 19
    