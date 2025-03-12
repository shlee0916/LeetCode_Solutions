'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        all_nodes = [root]
        res = []
        
        while all_nodes:
            node = all_nodes.pop()
            if node:
                res.append(node.val)
                all_nodes.append(node.left)
                all_nodes.append(node.right)
                
        return res[::-1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))