'''
https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
'''

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        ans = []
        if root is None:
            return ans
        
        stack = [root]
        while stack:
            cur_node = stack.pop()

            if cur_node.children:
                stack.extend(cur_node.children[::-1])

            ans.append(cur_node.val)

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    test1 = sol.preorder(test1_tree)
    assert test1 == [1, 3, 5, 6, 2, 4]
    