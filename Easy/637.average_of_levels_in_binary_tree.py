'''
https://leetcode.com/problems/average-of-levels-in-binary-tree/
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = [root]
        level_vals = []
        if root is None:
            return level_vals
        
        while que:
            loop_cnt = len(que)
            level_sum = 0
            for _ in range(loop_cnt):
                node = que.pop(0)
                level_sum += node.val
                
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
                    
            level_vals.append(level_sum / loop_cnt)
            
        return level_vals


if __name__ == "__main__":
    sol = Solution()

    test_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    print(sol.averageOfLevels(test_tree))