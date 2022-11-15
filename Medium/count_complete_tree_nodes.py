'''
https://leetcode.com/problems/count-complete-tree-nodes/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Brute force, DFS, O(n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        cnt = 0
        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            cnt += 1

        return cnt


# Binary search O(logN * logN)
# ref: https://leetcode.com/problems/count-complete-tree-nodes/solutions/701466/python-o-log-n-log-n-solution-with-binary-search-explained/
# Genius....
# Get depth and Find last layer's nodes by binary search
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Binary Search helper
        def check_path(node: Optional[TreeNode], num: int) -> bool:
            for s in bin(num)[3:]:
                if s == "0":
                    node = node.left
                else:
                    node = node.right
                
                if not node:
                    return False

            return True
        ############

        if not root:
            return 0

        left, depth = root, 0
        while left.left:
            left, depth = left.left, depth + 1

        begin, end = (1 << depth), (1 << (depth + 1)) - 1
        if check_path(root, end):
            return end

        while begin + 1 < end:
            mid = (begin + end) // 2

            if check_path(root, mid):
                begin = mid
            else:
                end = mid

        return begin


if __name__ == "__main__":
    sol = Solution()

    test_tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    test1 = sol.countNodes(test_tree1)
    print(test1, 6)
    assert test1 == 6

    test_tree2 = TreeNode(1)
    test2 = sol.countNodes(test_tree2)
    print(test2, 1)
    assert test2 == 1

    test_tree3 = None
    test3 = sol.countNodes(test_tree3)
    print(test3, 0)
    assert test3 == 0