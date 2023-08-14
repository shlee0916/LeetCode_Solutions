'''
https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
'''

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return

        ans = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            ans.append(cur_node.val)
            stack.extend(cur_node.children)

        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
    test1 = sol.postorder(test1_tree)
    assert test1 == [5, 6, 3, 2, 4, 1]
    
    test2_tree = Node(1, [Node(2, []), Node(3, [Node(6, []), Node(7, [Node(11, [Node(14, [])])])]), Node(4, [Node(8, [Node(12, [])])]), Node(5, [Node(9, [Node(13, [])]), Node(10, [])])])
    test2 = sol.postorder(test2_tree)
    assert test2 == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
    