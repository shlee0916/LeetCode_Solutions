'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        cur_node = root
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            k -= 1
            if k == 0:
                return cur_node.val

            cur_node = cur_node.right
            
            
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    test1 = sol.kthSmallest(test1_tree, 1)
    print(test1, 1)
    assert test1 == 1
    
    test2_tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    test2 = sol.kthSmallest(test2_tree, 3)
    print(test2, 3)
    assert test2 == 3
    