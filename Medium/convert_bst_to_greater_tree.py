'''
https://leetcode.com/problems/convert-bst-to-greater-tree/description/
'''

from collections import deque

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, val):
            if node is None:
                return val

            val = dfs(node.right, val)
            node.val += val

            return dfs(node.left, node.val)

        dfs(root, 0)

        return root


if __name__ == "__main__":
    # test helper #############
    def print_levels(root: TreeNode) -> List[Optional[int]]:
        if not root:
            return []
        
        que = deque([root])
        levels = []
        while que:
            cur_len = len(que)
            for _ in range(cur_len):
                cur_node = que.popleft()
                levels.append(cur_node.val)
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                
        return levels
    ############################
    sol = Solution()
    
    test1_tree = TreeNode(0, None, TreeNode(1))
    test1 = sol.convertBST(test1_tree)
    assert print_levels(test1) == [1, 1]
    
    test2_tree = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
    test2 = sol.convertBST(test2_tree)
    assert print_levels(test2) == [30, 36, 21, 36, 35, 26, 15, 33, 8]
    