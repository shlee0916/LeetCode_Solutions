'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        parents_map = {root: None}
        while (p not in parents_map) or (q not in parents_map):
            cur_node = stack.pop()

            if cur_node.left:
                parents_map[cur_node.left] = cur_node
                stack.append(cur_node.left)
            if cur_node.right:
                parents_map[cur_node.right] = cur_node
                stack.append(cur_node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents_map[p]
        
        while q not in ancestors:
            q = parents_map[q]

        return q


if __name__ == "__main__":
    sol = Solution()

    test1_p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    test1_q = TreeNode(1, TreeNode(0), TreeNode(8))
    test1_tree = TreeNode(3, test1_p, test1_q)
    test1 = sol.lowestCommonAncestor(root = test1_tree, p = test1_p, q = test1_q)
    assert test1.val == 3

    test2_q = TreeNode(4)
    test2_p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), test1_q))
    test2_tree = TreeNode(3, test2_p, TreeNode(1, TreeNode(0), TreeNode(8)))
    test2 = sol.lowestCommonAncestor(root = test2_tree, p = test2_p, q = test2_p)
    assert test2.val == 5

    test3_q = TreeNode(2)
    test3_p = TreeNode(1, test3_q)
    test3_tree = test3_p
    test3 = sol.lowestCommonAncestor(root = test3_tree, p = test3_p, q = test3_q)
    assert test3.val == 1
