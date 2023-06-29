'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
'''

from collections import defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x = 0, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return

        graph = defaultdict(list)
        stack = [root]
        
        while stack:
            cur_node = stack.pop()
            if cur_node.left:
                graph[cur_node].append(cur_node.left)
                graph[cur_node.left].append(cur_node)
                stack.append(cur_node.left)
            if cur_node.right:
                graph[cur_node].append(cur_node.right)
                graph[cur_node.right].append(cur_node)
                stack.append(cur_node.right)

        ans = []
        stack = [(target, k)]
        visit = set([target])
        while stack:
            cur_node, dist = stack.pop()
            if dist == 0:
                ans.append(cur_node.val)
            else:
                for next_node in graph[cur_node]:
                    if next_node not in visit:
                        visit.add(next_node)
                        stack.append((next_node, dist - 1))

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    target = test1_tree.left
    test1 = sol.distanceK(test1_tree, target = target, k = 2)
    assert set(test1) == set([7, 4, 1])
    
    test2_tree = TreeNode(1)
    test2 = sol.distanceK(test2_tree, target = test2_tree, k = 3)
    assert test2 == []
    