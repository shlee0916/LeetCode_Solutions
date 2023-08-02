'''
https://leetcode.com/problems/univalued-binary-tree/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        values = set()
        stack = [root]
        while stack:
            cur_node = stack.pop()

            values.add(cur_node.val)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

        return len(values) == 1


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
    test1 = sol.isUnivalTree(test1_tree)
    assert test1 == True
    
    test2_tree = TreeNode(2, TreeNode(2, TreeNode(5), TreeNode(2)), TreeNode(2))
    test2 = sol.isUnivalTree(test2_tree)
    assert test2 == False
    