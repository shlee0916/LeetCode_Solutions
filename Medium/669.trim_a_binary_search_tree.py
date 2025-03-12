'''
https://leetcode.com/problems/trim-a-binary-search-tree/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


if __name__ == "__main__":
    # Test helper
    def print_levels(root: TreeNode) -> List[Optional[int]]:
        if not root:
            return []
        
        que = [root]
        levels = []
        while que:
            cur_len = len(que)
            cur_level = []
            for _ in range(cur_len):
                cur_node = que.pop(0)
                cur_level.append(cur_node.val)
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            
            levels.append(cur_level)

        return levels
    #############################
    
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(0), TreeNode(2))
    test1 = sol.trimBST(root = test1_tree, low = 1, high = 2)
    assert print_levels(test1) == [[1], [2]]
    
    test2_tree = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
    test2 = sol.trimBST(root = test2_tree, low = 1, high = 3)
    assert print_levels(test2) == [[3], [2], [1]]
    