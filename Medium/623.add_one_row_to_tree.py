'''
https://leetcode.com/problems/add-one-row-to-tree/
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:        
        if depth == 1:
            new_node = TreeNode(val, root)
            return new_node
        
        stack = [(root, 1)]
        while stack:
            cur_node, cur_depth = stack.pop()
            cur_depth += 1
            
            if cur_depth == depth:
                new_node = TreeNode(val, cur_node.left)
                cur_node.left = new_node

                new_node = TreeNode(val, None, cur_node.right)
                cur_node.right = new_node
            else:
                if cur_node.left:
                    stack.append((cur_node.left, cur_depth))
                if cur_node.right:
                    stack.append((cur_node.right, cur_depth))
                    
        return root


if __name__ == "__main__":
    def travel(tree: TreeNode):
        stack = [tree]
        while stack:
            cur_node = stack.pop()

            print(cur_node.val, end = " ")
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        
        print()

    sol = Solution()


    test_tree1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    test_result1 = sol.addOneRow(test_tree1, 5, 4)
    travel(test_result1)

    test_tree2 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
    test_result2 = sol.addOneRow(test_tree2, 1, 1)
    travel(test_result2)