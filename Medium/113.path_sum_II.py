'''
https://leetcode.com/problems/path-sum-ii/
'''
from typing import Optional, List
from copy import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return None
        
        stack = [(root, [root.val])]
        ans = []
        while stack:
            cur_node, path_val = stack.pop()
            # print(path_val)
            if cur_node.left is None and cur_node.right is None:
                if sum(path_val) == targetSum:
                    ans.append(path_val[:])    
            else:
                if cur_node.left:
                    sub_val = path_val[:]
                    sub_val.append(cur_node.left.val)
                    stack.append((cur_node.left, sub_val))
                if cur_node.right:
                    sub_val = path_val[:]
                    sub_val.append(cur_node.right.val)
                    stack.append((cur_node.right, sub_val))
        
        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test_tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    
    print(sol.pathSum(test_tree, 22))