'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        que = [root]
        level_depth = 1
        res = []
        while que:
            cur_level = []
            for _ in range(len(que)):
                cur_node = que.pop(0)
                cur_level.append(cur_node.val)

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

            if level_depth % 2 == 0:
                res.append(cur_level[::-1])
            else:
                res.append(cur_level)

            level_depth += 1

        return res


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    test1 = sol.zigzagLevelOrder(test1_tree)
    print(test1, [[3],[20,9],[15,7]])
    assert test1 == [[3],[20,9],[15,7]]

    test2_tree = TreeNode(1)
    test2 = sol.zigzagLevelOrder(test2_tree)
    print(test2, [[1]])
    assert test2 == [[1]]

    test3_tree = None
    test3 = sol.zigzagLevelOrder(test3_tree)
    print(test3, None)
    assert test3 == None
