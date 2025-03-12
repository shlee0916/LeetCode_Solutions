'''
https://leetcode.com/problems/range-sum-of-bst/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        
        res = 0
        stack = [root]
        while stack:
            cur_node = stack.pop()

            if cur_node.val > low and cur_node.left:
                stack.append(cur_node.left)
            if cur_node.val < high and cur_node.right:
                stack.append(cur_node.right)
            if low <= cur_node.val <= high:
                res += cur_node.val

        return res
        

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    test1 = sol.rangeSumBST(test1_tree, 7, 15)
    print(test1, 32)
    assert test1 == 32

    test2_tree = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))), TreeNode(15, TreeNode(13), TreeNode(18)))
    test2 = sol.rangeSumBST(test2_tree, 6, 10)
    print(test2, 23)
    assert test2 == 23
