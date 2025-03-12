'''
https://leetcode.com/problems/merge-two-binary-trees/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2


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
    
    test1_tree1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    test1_tree2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    test1 = sol.mergeTrees(test1_tree1, test1_tree2)
    assert print_levels(test1) == [3, 4, 5, 5, 4, 7]
    
    test2_tree1 = TreeNode(1)
    test2_tree2 = TreeNode(1, TreeNode(2))
    test2 = sol.mergeTrees(test2_tree1, test2_tree2)
    assert print_levels(test2) == [2, 2]
    