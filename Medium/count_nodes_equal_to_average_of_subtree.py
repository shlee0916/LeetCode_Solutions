'''
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
'''

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0


    # Recursive
    def get_subtree(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return 0, 0

        left_sum, left_cnt = self.get_subtree(root.left)
        right_sum, right_cnt = self.get_subtree(root.right)

        total_vals = left_sum + right_sum + root.val
        total_cnt = left_cnt + right_cnt + 1

        if total_vals // total_cnt == root.val:
            self.result += 1

        return total_vals, total_cnt


    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.get_subtree(root)

        return self.result
    

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
    test1 = sol.averageOfSubtree(test1_tree)
    print(test1, 5)
    assert test1 == 5

    # re-Define for init self.result
    sol = Solution()

    test2_tree = TreeNode(1)
    test2 = sol.averageOfSubtree(test2_tree)
    print(test2, 1)
    assert test2 == 1
