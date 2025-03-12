'''
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        cur_node = root
        stack = []
        acc_sum = 0
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.right

            cur_node = stack.pop()
            cur_node.val += acc_sum
            acc_sum = cur_node.val
            cur_node = cur_node.left

        return root
        
        
if __name__ == "__main__":
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
            
            
    sol = Solution()
    
    test1_tree = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
    test1 = sol.bstToGst(test1_tree)
    test1_res = print_levels(test1)
    print(test1_res, [30, 36, 21, 36, 35, 26, 15, 33, 8])
    assert test1_res == [30, 36, 21, 36, 35, 26, 15, 33, 8]
    
    test2_tree = TreeNode(0, None, TreeNode(1))
    test2 = sol.bstToGst(test2_tree)
    test2_res = print_levels(test2)
    print(test2_res, [1, 1])
    assert test2_res == [1, 1]
    