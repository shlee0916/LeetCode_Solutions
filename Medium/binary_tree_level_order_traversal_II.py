'''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = [root]
        res = []
        while que:
            iter_len = len(que)
            cur_level = []
            for _ in range(iter_len):
                cur_node = que.pop(0)

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

                cur_level.append(cur_node.val)

            res.append(cur_level)

        return res[::-1]


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    test1 = sol.levelOrderBottom(test1_tree)
    print(test1, [[15, 7], [9, 20], [3]])
    assert test1 == [[15, 7], [9, 20], [3]]

    test2_tree = TreeNode(1)
    test2 = sol.levelOrderBottom(test2_tree)
    print(test2, [[1]])
    assert test2 == [[1]]

    test3_tree = None
    test3 = sol.levelOrderBottom(test3_tree)
    print(test3, [])
    assert test3 == []
    