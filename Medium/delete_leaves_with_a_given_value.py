'''
https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)

            if node.left:
                if node.left.val == target and node.left.left is None and node.left.right is None:
                    node.left = None
            
            if node.right:
                if node.right.val == target and node.right.left is None and node.right.right is None:
                    node.right = None
            
        dfs(root)

        return None if root.val == target and root.left is None and root.right is None else root
    
    
if __name__ == "__main__":
    # test helper
    def print_levels(root: TreeNode) -> List[Optional[int]]:
        if not root:
            return []
        
        que = [root]
        levels = []
        while que:
            cur_len = len(que)
            for _ in range(cur_len):
                cur_node = que.pop(0)
                levels.append(cur_node.val)
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                
        return levels
    ############################
    
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4)))
    test1 = sol.removeLeafNodes(root = test1_tree, target = 2)
    print(print_levels(test1))
    
    test2_tree = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3))
    test2 = sol.removeLeafNodes(root = test2_tree, target = 3)
    print(print_levels(test2))
    
    test3_tree = TreeNode(1, TreeNode(2, TreeNode(2, TreeNode(2))))
    test3 = sol.removeLeafNodes(root = test3_tree, target = 2)
    print(print_levels(test3))
    