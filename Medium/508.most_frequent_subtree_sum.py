'''
https://leetcode.com/problems/most-frequent-subtree-sum/description/
'''

from collections import defaultdict

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        frequency = defaultdict(int)

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            subtree_sum = node.val + left + right
            frequency[subtree_sum] += 1

            return subtree_sum

        dfs(root)
        max_frequency = max(frequency.values())
        
        return [key for key, value in frequency.items() if value == max_frequency]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(5, TreeNode(2), TreeNode(-3))
    test1 = sol.findFrequentTreeSum(test1_tree)
    assert test1 == [2, -3, 4]
    
    test2_tree = TreeNode(5, TreeNode(2), TreeNode(-5))
    test2 = sol.findFrequentTreeSum(test2_tree)
    assert test2 == [2]
    