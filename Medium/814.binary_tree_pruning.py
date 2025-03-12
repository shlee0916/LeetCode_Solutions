'''
https://leetcode.com/problems/binary-tree-pruning/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur_node: Optional[TreeNode]):
            if cur_node is None:
                return True

            left = dfs(cur_node.left)
            right = dfs(cur_node.right)

            if left:
                cur_node.left = None
            if right:
                cur_node.right = None

            return left and right and cur_node.val == 0

        return root if not dfs(root) else None
        

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

    test1_tree = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
    test1 = sol.pruneTree(test1_tree)
    test1_res = print_levels(test1)
    assert test1_res == [1, 0, 1]

    test2_tree = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
    test2 = sol.pruneTree(test2_tree)
    test2_res = print_levels(test2)
    assert test2_res == [1, 1, 1]

    test3_tree = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(0)), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1)))
    test3 = sol.pruneTree(test3_tree)
    test3_res = print_levels(test3)
    assert test3_res == [1, 1, 0 ,1, 1, 1]
