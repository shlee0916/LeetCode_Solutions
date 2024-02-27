'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root_idx = inorder.index(preorder.pop(0))

            root_node = TreeNode(inorder[root_idx])
            root_node.left = self.buildTree(preorder, inorder[0 : root_idx])
            root_node.right = self.buildTree(preorder, inorder[root_idx + 1 :])

            return root_node


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
    
    test1 = sol.buildTree(preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7])
    assert print_levels(test1) == [3, 9, 20, 15, 7]

    test2 = sol.buildTree(preorder = [-1], inorder = [-1])
    assert print_levels(test2) == [-1]
