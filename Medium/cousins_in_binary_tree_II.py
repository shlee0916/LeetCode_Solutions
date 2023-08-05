'''
https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, depth: int) -> None:
            if node:
                if len(level_sum) == depth:
                    level_sum[depth] = 0

                level_sum[depth] += node.val

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)


        def sum_dfs(node: TreeNode, depth: int) -> None:
            if node:
                node.val = level_sum[depth] - node.val

                if node.left and node.right:
                    cousins_sum = node.left.val + node.right.val
                    node.left.val = node.right.val = cousins_sum

                sum_dfs(node.left, depth + 1)
                sum_dfs(node.right, depth + 1)

        level_sum = {}
        dfs(root, 0)
        sum_dfs(root, 0)

        return root
    
    
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
    
    test1_tree = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, None, TreeNode(7)))
    test1 = sol.replaceValueInTree(test1_tree)
    assert print_levels(test1) == [0, 0, 0, 7, 7, 11]
    
    test2_tree = TreeNode(3, TreeNode(1), TreeNode(2))
    test2 = sol.replaceValueInTree(test2_tree)
    assert print_levels(test2) == [0, 0 ,0]
