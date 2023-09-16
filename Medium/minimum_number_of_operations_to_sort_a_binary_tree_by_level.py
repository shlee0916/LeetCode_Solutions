'''
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return

        ans = 0
        que = deque([root])
        while que:
            level = []
            for node in que:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            cur_level = [(value, idx) for idx, value in enumerate([node.val for node in level])]
            sorted_idx = [idx for _, idx in sorted(cur_level)]

            for idx in range(len(sorted_idx)):
                while sorted_idx[idx] != idx:
                    next_idx = sorted_idx[idx]
                    sorted_idx[idx], sorted_idx[next_idx] = sorted_idx[next_idx], sorted_idx[idx]
                    ans += 1

            que = level

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(4, TreeNode(7), TreeNode(6)), TreeNode(3, TreeNode(8, TreeNode(9)), TreeNode(5, TreeNode(10))))
    test1 = sol.minimumOperations(test1_tree)
    assert test1 == 3
    
    test2_tree = TreeNode(1, TreeNode(3, TreeNode(7), TreeNode(6)), TreeNode(2, TreeNode(5), TreeNode(4)))
    test2 = sol.minimumOperations(test2_tree)
    assert test2 == 3
    
    test3_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    test3 = sol.minimumOperations(test3_tree)
    assert test3 == 0
    