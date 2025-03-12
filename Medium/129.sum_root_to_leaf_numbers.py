'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        stack = [(root, f"{root.val}")]
        
        ans = []
        while stack:
            cur_node, cur_val = stack.pop()
            
            if cur_node.left:
                stack.append((cur_node.left, cur_val + f"{cur_node.left.val}"))
            if cur_node.right:
                stack.append((cur_node.right, cur_val + f"{cur_node.right.val}"))
                
            if not cur_node.left and not cur_node.right:
                ans.append(cur_val)
                
        return sum(map(int, ans))


if __name__ == "__main__":
    sol = Solution()

    test_tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    test_tree2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))

    print(sol.sumNumbers(test_tree1), 25)
    print(sol.sumNumbers(test_tree2), 1026)