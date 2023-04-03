'''
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        que = deque([root])
        level_sum = []
        while que:
            cur_level = 0
            for _ in range(len(que)):
                cur_node = que.popleft()
                cur_level += cur_node.val

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

            level_sum.append(cur_level)

        return level_sum.index(max(level_sum)) + 1
    

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    test1 = sol.maxLevelSum(test1_tree)
    assert test1 == 2

    test2_tree = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))
    test2 = sol.maxLevelSum(test2_tree)
    assert test2 == 2
    