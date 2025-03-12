'''
https://leetcode.com/problems/all-possible-full-binary-trees/description/
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        res = []
        for idx in range(1, n, 2):
            for left in self.allPossibleFBT(idx):
                for right in self.allPossibleFBT(n - 1 - idx):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.allPossibleFBT(7)
    print(test1)
    
    test2 = sol.allPossibleFBT(3)
    print(test2)
    