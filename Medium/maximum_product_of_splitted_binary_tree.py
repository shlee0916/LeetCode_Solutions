'''
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sub_tree_sums = []

        def sub_sum(node):
            if node:
                tmp_sum = node.val + sub_sum(node.left) + sub_sum(node.right)
                self.sub_tree_sums.append(tmp_sum)
            else:
                return 0

            return tmp_sum

        total_sum = sub_sum(root)
        ans = max((total_sum - val) * val for val in self.sub_tree_sums) % (10**9 + 7)
        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    test1 = sol.maxProduct(test1_tree)
    print(test1, 110)
    assert test1 == 110
    
    test2_tree = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
    test2 = sol.maxProduct(test2_tree)
    print(test2, 90)
    assert test2 == 90
    