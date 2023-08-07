'''
http://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        # Find deepest nodes
        parents = {}
        que = deque([root])
        while que:
            deepest_nodes = []

            for _ in range(len(que)):
                cur_node = que.popleft()
                deepest_nodes.append(cur_node)

                if cur_node.left:
                    parents[cur_node.left] = cur_node
                    que.append(cur_node.left)
                if cur_node.right:
                    parents[cur_node.right] = cur_node
                    que.append(cur_node.right)

        while len(deepest_nodes) > 1:
            common = set()

            for node in deepest_nodes:
                common.add(parents[node])

            deepest_nodes = list(common)

        return deepest_nodes[0]


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    test1 = sol.subtreeWithAllDeepest(test1_tree)
    assert test1.val == 2
    
    test2_tree = TreeNode(1)
    test2 = sol.subtreeWithAllDeepest(test2_tree)
    assert test2.val == 1
    
    test3_tree = TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3))
    test3 = sol.subtreeWithAllDeepest(test3_tree)
    assert test3.val == 2
    