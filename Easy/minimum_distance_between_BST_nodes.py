'''
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    pre = -float("inf")
    res = float("inf")

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        self.minDiffInBST(root.left)

        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        self.minDiffInBST(root.right)

        return self.res
            
            
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    test1 = sol.minDiffInBST(test1_tree)
    print(test1, 1)
    assert test1 == 1
    
    sol = Solution()
    test2_tree = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
    test2 = sol.minDiffInBST(test2_tree)
    print(test2, 1)
    assert test2 == 1
    