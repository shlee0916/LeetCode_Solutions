'''
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        que = deque([(original, cloned)])
        while que:
            ori_node, clone_node = que.popleft()

            if ori_node == target:
                return clone_node

            if ori_node.left:
                que.append((ori_node.left, clone_node.left))
            if ori_node.right:
                que.append((ori_node.right, clone_node.right))


if __name__ == "__main__":
    sol = Solution()

    target_node = TreeNode(3, TreeNode(6), TreeNode(19))
    test1_ori = TreeNode(7, TreeNode(4), target_node)
    clone_target_node = TreeNode(3, TreeNode(6), TreeNode(19))
    test2_clone = TreeNode(7, TreeNode(4), clone_target_node)
    test1 = sol.getTargetCopy(original = test1_ori, cloned = test2_clone, target = target_node)
    assert test1 == clone_target_node
    