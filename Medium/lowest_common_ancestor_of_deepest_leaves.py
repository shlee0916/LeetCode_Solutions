'''
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
'''

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        parents = {}
        que = deque([root])
        while que:
            last_level = []

            for _ in range(len(que)):
                cur_node = que.popleft()
                last_level.append(cur_node)

                if cur_node.left:
                    que.append(cur_node.left)
                    parents[cur_node.left] = cur_node

                if cur_node.right:
                    que.append(cur_node.right)
                    parents[cur_node.right] = cur_node

        while len(last_level) > 1:
            common_ancestor = set()

            for node in last_level:
                common_ancestor.add(parents[node])

            last_level = list(common_ancestor)
            
        return last_level[0]


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    test1 = sol.lcaDeepestLeaves(test1_tree)
    assert test1.val == 2
    
    test2_tree = TreeNode(1)
    test2 = sol.lcaDeepestLeaves(test2_tree)
    assert test2.val == 1
    
    test3_tree = TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3))
    test3 = sol.lcaDeepestLeaves(test3_tree)
    assert test3.val == 2
    