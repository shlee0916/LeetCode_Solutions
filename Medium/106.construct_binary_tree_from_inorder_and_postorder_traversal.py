'''
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        stack, inorder_idx = [root], len(inorder) - 1

        for post_val in postorder[:-1][::-1]:
            if stack[-1].val == inorder[inorder_idx]:
                cur_node = stack[-1]
                
                while stack and stack[-1].val == inorder[inorder_idx]:
                    cur_node = stack.pop()
                    inorder_idx -= 1

                if inorder_idx >= 0:
                    cur_node.left = left = TreeNode(post_val)
                    stack.append(left)

            else:
                stack[-1].right = right = TreeNode(post_val)
                stack.append(right)

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
    
    test1 = sol.buildTree(inorder = [9, 3, 15, 20, 7],  postorder = [9, 15, 7, 20, 3])
    test1_res = print_levels(test1)
    print(test1_res)
    
    test2 = sol.buildTree(inorder = [-1], postorder = [-1])
    test2_res = print_levels(test2)
    print(test2_res)
    