'''
https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
'''

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        que = deque([root])
        level = 0
        while que:
            level_len = len(que)
            if level % 2 == 1:
                left = 0
                right = level_len - 1
                while left < right:
                    que[left].val, que[right].val = que[right].val, que[left].val
                    left += 1
                    right -= 1

            for _ in range(level_len):
                cur_node = que.popleft()
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                
            level += 1
            
        return root


if __name__ == "__main__":
    # Test helper
    def print_levels(root: TreeNode) -> List[Optional[int]]:
        if not root:
            return []
        
        que = [root]
        levels = []
        while que:
            cur_len = len(que)
            cur_level = []
            for _ in range(cur_len):
                cur_node = que.pop(0)
                cur_level.append(cur_node.val)
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            
            levels.append(cur_level)

        return levels
    #############################

    sol = Solution()

    test1_tree = TreeNode(2, TreeNode(3, TreeNode(8), TreeNode(13)), TreeNode(5, TreeNode(21), TreeNode(34)))
    test1 = sol.reverseOddLevels(test1_tree)
    assert print_levels(test1) == [[2], [5, 3], [8, 13, 21, 34]]

    test2_tree = TreeNode(7, TreeNode(13), TreeNode(11))
    test2 = sol.reverseOddLevels(test2_tree)
    assert print_levels(test2) == [[7], [11, 13]]
