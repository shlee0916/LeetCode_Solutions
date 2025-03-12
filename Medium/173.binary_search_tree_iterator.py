'''
https://leetcode.com/problems/binary-search-tree-iterator/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.__push(root)
        

    def next(self) -> int:
        cur_node = self.stack.pop()
        self.__push(cur_node.right)
        return cur_node.val
        

    def hasNext(self) -> bool:
        return self.stack
    
    
    def __push(self, node):
        while node:
            self.stack.append(node)
            node = node.left


if __name__ == "__main__":
    test_tree = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    
    bsti = BSTIterator(test_tree)
    
    while bsti.hasNext():
        print(bsti.next())