'''
https://leetcode.com/problems/binary-tree-right-side-view/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        ans = []
        que = [root]
        while que:
            cur_level = []
            for _ in range(len(que)):
                cur_node = que.pop(0)
                cur_level.append(cur_node.val)

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

            ans.append(cur_level[-1])

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1_tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    test1 = sol.rightSideView(test1_tree)   
    print(test1, [1, 3, 4])
    assert test1 == [1, 3, 4]

    test2_tree = TreeNode(1, None, TreeNode(3))
    test2 = sol.rightSideView(test2_tree)
    print(test2, [1, 3])
    assert test2 == [1, 3]

    test3_tree = None
    test3 = sol.rightSideView(test3_tree)
    print(test3, None)
    assert test3 == None
