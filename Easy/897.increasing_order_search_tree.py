'''
https://leetcode.com/problems/increasing-order-search-tree/description/
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recursive(root, tail):
            if root is None:
                return tail

            res = recursive(root.left, root)
            root.left = None
            root.right = recursive(root.right, tail)

            return res

        return recursive(root, None)
    
    
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
    
    test1_tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
    test1 = sol.increasingBST(test1_tree)
    assert print_levels(test1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    test2_tree = TreeNode(5, TreeNode(1), TreeNode(7))
    test2 = sol.increasingBST(test2_tree)
    assert print_levels(test2) == [1, 5, 7]
    