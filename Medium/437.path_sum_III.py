'''
https://leetcode.com/problems/path-sum-iii/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        paths = {0: 1}

        def dfs(node, cur_sum):
            if node is None:
                return
            
            cur_sum += node.val
            pre_sum = cur_sum - targetSum

            self.ans += paths.get(pre_sum, 0)
            paths[cur_sum] = paths.get(cur_sum, 0) + 1

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            paths[cur_sum] -= 1

        dfs(root, 0)

        return self.ans


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    test1 = sol.pathSum(test1_tree, 8)
    assert test1 == 3

    test2_tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    test2 = sol.pathSum(test2_tree, 22)
    assert test2 == 3
