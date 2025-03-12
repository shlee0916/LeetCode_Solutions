'''
https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        que = [root]
        while que:
            cur_node = que.pop(0)

            if cur_node is None:
                if any(que):
                    return False
            else:
                que.append(cur_node.left)
                que.append(cur_node.right)

        return True
    

if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    test1 = sol.isCompleteTree(test1_tree)
    print(test1, True)
    assert test1 == True

    test2_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
    test2 = sol.isCompleteTree(test2_tree)
    print(test2, False)
    assert test2 == False
    