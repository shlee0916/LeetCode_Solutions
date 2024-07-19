'''
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/?envType=daily-question&envId=2024-07-18
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def dfs(node):
            if node is None:
                return []

            if node.left is None and node.right is None:
                return [1]

            left_nodes = dfs(node.left)
            right_nodes = dfs(node.right)

            self.ans += sum(left + right <= distance for left in left_nodes for right in right_nodes)

            return [node + 1 for node in left_nodes + right_nodes if node + 1 < distance]

        dfs(root)

        return self.ans


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    test1 = sol.countPairs(test1_tree, 3)
    assert test1 == 1

    test2_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    test2 = sol.countPairs(test2_tree, 3)
    assert test2 == 2
    