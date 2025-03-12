'''
https://leetcode.com/problems/balance-a-binary-search-tree/description/
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        all_nodes = []

        def inorder_node(root):
            if root is None:
                return

            inorder_node(root.left)
            all_nodes.append(root)
            inorder_node(root.right)

        def rebuild_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = all_nodes[mid]
            root.left = rebuild_tree(left, mid - 1)
            root.right = rebuild_tree(mid + 1, right)

            return root

        inorder_node(root)

        return rebuild_tree(0, len(all_nodes) - 1)
    

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
    
    test1_tree = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    test1 = sol.balanceBST(test1_tree)
    print(print_levels(test1))

    
    test2_tree = TreeNode(2, TreeNode(1), TreeNode(3))
    test2 = sol.balanceBST(test2_tree)
    print(print_levels(test2))
    