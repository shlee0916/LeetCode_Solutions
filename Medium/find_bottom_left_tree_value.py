'''
https://leetcode.com/problems/find-bottom-left-tree-value/description/
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        
        que = deque([root])
        most_left = 0
        while que:
            cur_node = que.popleft()
            most_left = cur_node.val
            if cur_node.right:
                que.append(cur_node.right)
            if cur_node.left:
                que.append(cur_node.left)

        return most_left
    

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(2, TreeNode(1), TreeNode(3))
    test1 = sol.findBottomLeftValue(test1_tree)
    assert test1 == 1

    test2_tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    test2 = sol.findBottomLeftValue(test2_tree)
    assert test2 == 7
