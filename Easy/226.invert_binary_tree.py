'''
https://leetcode.com/problems/invert-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        dummy = root.left
        root.left = root.right
        root.right = dummy

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

if __name__ == "__main__":
    def tree2list(root):
        values = []
        
        que = [root]
        while que:
            level_len = len(que)
            for _ in range(level_len):
                cur_node = que.pop()
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                    
                values.append(cur_node.val)
                        
        return values
            
    
    sol = Solution()
    
    test1_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    test1 = sol.invertTree(test1_tree)
    test1_res = tree2list(test1)
    print(test1_res)
    
    test2_tree = TreeNode(2, TreeNode(1), TreeNode(3))
    test2 = sol.invertTree(test2_tree)
    test2_res = tree2list(test2)
    print(test2_res)
    