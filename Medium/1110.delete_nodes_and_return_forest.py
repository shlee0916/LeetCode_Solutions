'''
https://leetcode.com/problems/delete-nodes-and-return-forest/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete_set = set(to_delete)

        def dfs(root, is_root):
            if not root:
                return None

            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                ans.append(root)

            root.left = dfs(root.left, root_deleted)
            root.right = dfs(root.right, root_deleted)
            
            return None if root_deleted else root

        dfs(root, True)

        return ans


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
    
    test1_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    test1 = sol.delNodes(test1_tree, [3, 5])
    test1_res = [print_levels(test1_root) for test1_root in test1]
    assert test1_res == [[1, 2, 4], [6], [7]]
    
    test2_tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))
    test2 = sol.delNodes(test2_tree, [3])
    test2_res = [print_levels(test2_root) for test2_root in test2]
    assert test2_res == [[1, 2, 4]]
    