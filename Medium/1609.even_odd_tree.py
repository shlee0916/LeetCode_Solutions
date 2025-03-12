'''
https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        level = 0
        que = deque([root])

        while que:
            prev_val = None

            for _ in range(len(que)):
                cur_node = que.popleft()

                if ((level % 2 == 0 and (cur_node.val % 2 == 0 or (prev_val is not None and cur_node.val <= prev_val))) or 
                (level % 2 == 1 and (cur_node.val % 2 == 1 or (prev_val is not None and cur_node.val >= prev_val)))):
                    return False
                
                prev_val = cur_node.val

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

            level += 1

        return True
                

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(10, TreeNode(3, TreeNode(12), TreeNode(8))), TreeNode(4, TreeNode(7, TreeNode(6)), TreeNode(9, None, TreeNode(2))))
    test1 = sol.isEvenOddTree(test1_tree)
    assert test1 == True

    test2_tree = TreeNode(5, TreeNode(4, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(7)))
    test2 = sol.isEvenOddTree(test2_tree)
    assert test2 == False

    test3_tree = TreeNode(5, TreeNode(9, TreeNode(3), TreeNode(5)), TreeNode(1, TreeNode(7)))
    test3 = sol.isEvenOddTree(test3_tree)
    assert test3 == False
