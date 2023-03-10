'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good_nodes_num = 0
        deq = deque([(root, -float("inf"))])
        while deq:
            cur_node, max_val = deq.popleft()

            if cur_node.val >= max_val:
                good_nodes_num += 1

            if cur_node.left:
                deq.append((cur_node.left, max(cur_node.val, max_val)))
            if cur_node.right:
                deq.append((cur_node.right, max(cur_node.val, max_val)))

        return good_nodes_num 


if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    test1 = sol.goodNodes(test1_tree)
    print(test1, 4)
    assert test1 == 4
    
    test2_tree = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    test2 = sol.goodNodes(test2_tree)
    print(test2, 3)
    assert test2 == 3
    