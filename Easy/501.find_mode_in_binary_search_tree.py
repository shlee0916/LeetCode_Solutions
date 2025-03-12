'''
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/?envType=daily-question&envId=2023-11-01
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = []
    max_cnt = 0
    cur_cnt = 0
    prev = 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return

            dfs(node.left)
            
            if node.val == self.prev:
                self.cur_cnt += 1
            else:
                self.cur_cnt = 1
            
            if self.cur_cnt > self.max_cnt:
                self.max_cnt = self.cur_cnt
                self.res = [node.val]
            elif self.cur_cnt == self.max_cnt:
                self.res.append(node.val)

            self.prev = node.val
            dfs(node.right)

        dfs(root)

        return self.res


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, None, TreeNode(2, TreeNode(2)))
    test1 = sol.findMode(test1_tree)
    assert test1 == [2]

    sol = Solution()
    test2_tree = TreeNode(0)
    test2 = sol.findMode(test2_tree)
    assert test2 == [0]
