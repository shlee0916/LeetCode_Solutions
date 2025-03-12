'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level_queue = []
        if root is not None:
            level_queue = [[root]]
            while level_queue:
                cur_level = level_queue.pop(0)
                next_level = []
                tmp_result = []
                for node in cur_level:
                    tmp_result.append(node.val)
                    if node.left is not None:
                        next_level.append(node.left)
                    if node.right is not None:
                        next_level.append(node.right)

                if tmp_result:
                    result.append(tmp_result)

                if next_level:
                    level_queue.append(next_level)
            
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    # TestCase 1
    test1 = TreeNode(1)
    print(sol.levelOrder(test1), [[1]])
    
    # TestCase 2
    test2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.levelOrder(test2), [[3],[9,20],[15,7]])
    
    # TestCase 3
    test3 = None
    print(sol.levelOrder(test3), [])