'''
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[None]):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0

        return 1 + max((self.maxDepth(child) for child in root.children), default = 0)


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    test1 = sol.maxDepth(test1_tree)
    assert test1 == 3
    
    test2_tree = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
    test2 = sol.maxDepth(test2_tree)
    assert test2 == 5
    