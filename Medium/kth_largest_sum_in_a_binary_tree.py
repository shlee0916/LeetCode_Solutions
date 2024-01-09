'''
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 
        
        level_sums = []
        que = deque([root])
        while que:
            cur_level = 0
            for _ in range(len(que)):
                cur_node = que.popleft()

                cur_level += cur_node.val

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

            level_sums.append(cur_level)

        return sorted(level_sums)[-k] if len(level_sums) >= k else -1


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
    test1 = sol.kthLargestLevelSum(root = test1_tree, k = 2)
    assert test1 == 13

    test2_tree = TreeNode(1, TreeNode(2, TreeNode(3)))
    test2 = sol.kthLargestLevelSum(root = test2_tree, k = 1)
    assert test2 == 3
