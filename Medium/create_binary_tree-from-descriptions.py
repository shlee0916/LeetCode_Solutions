'''
https://leetcode.com/problems/create-binary-tree-from-descriptions/description/
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()

        for parent, child, is_left in descriptions:
            parent_node = node_map.setdefault(parent, TreeNode(parent))
            child_node = node_map.setdefault(child, TreeNode(child))

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            children.add(child_node)

        root = set(node_map.values()) - children

        return root.pop()


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

    test1 = sol.createBinaryTree(descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
    test1_res = print_levels(test1)
    assert test1_res == [50, 20, 80, 15, 17, 19]

    test2 = sol.createBinaryTree(descriptions = [[1,2,1],[2,3,0],[3,4,1]])
    test2_res = print_levels(test2)
    assert test2_res == [1, 2, 3, 4]
    