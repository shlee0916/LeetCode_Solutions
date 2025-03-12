'''
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, None)]
        while stack:
            cur_node, parents = stack.pop()

            if cur_node.left:
                stack.append((cur_node.left, cur_node))
                if parents and parents.val % 2 == 0:
                    res += cur_node.left.val

            if cur_node.right:
                stack.append((cur_node.right, cur_node))
                if parents and parents.val % 2 == 0:
                    res += cur_node.right.val

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
    test1 = sol.sumEvenGrandparent(test1_tree)
    print(test1, 18)
    assert test1 == 18
    
    test2_tree = TreeNode(1)
    test2 = sol.sumEvenGrandparent(test2_tree)
    print(test2, 0)
    assert test2 == 0
    