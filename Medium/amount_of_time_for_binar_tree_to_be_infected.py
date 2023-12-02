'''
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
'''

from collections import defaultdict, deque

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        stack = [(root, None)]
        while stack:
            cur_node, cur_parent = stack.pop()

            if cur_parent:
                graph[cur_parent.val].append(cur_node.val)
                graph[cur_node.val].append(cur_parent.val)

            if cur_node.left:
                stack.append((cur_node.left, cur_node))
            if cur_node.right:
                stack.append((cur_node.right, cur_node))

        ans = -1
        visit = set([start])
        que = deque([start])
        while que:
            for _ in range(len(que)):
                cur_node = que.popleft()

                for next_node in graph[cur_node]:
                    if next_node not in visit:
                        visit.add(next_node)
                        que.append(next_node)

            ans += 1

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(6)))
    test1 = sol.amountOfTime(test1_tree, 3)
    assert test1 == 4
    
    test2_tree = TreeNode(1)
    test2 = sol.amountOfTime(test2_tree, 1)
    assert test2 == 0
    