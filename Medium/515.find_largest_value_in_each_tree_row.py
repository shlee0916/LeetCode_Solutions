'''
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
# Recursive
class Solution:
    def bfs(self, node: Optional[TreeNode], level: int) -> None:
        if not node:
            return

        if len(self.ans) == level:
            self.ans.append(node.val)
        else:
            self.ans[level] = max(self.ans[level], node.val)

        self.bfs(node.left, level + 1)
        self.bfs(node.right, level + 1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.bfs(root, 0)

        return self.ans        


# Iteration
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return

        que = [root]

        while que:
            cur_level = []
            for _ in range(len(que)):
                cur_node = que.pop(0)
                cur_level.append(cur_node)

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

            ans.append(max(node.val for node in cur_level))

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1_tree = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    test1 = sol.largestValues(test1_tree)
    print(test1, [1, 3, 9])
    assert test1 == [1, 3, 9]
    
    test2_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    test2 = sol.largestValues(test2_tree)
    print(test2, [1, 3])
    assert test2 == [1, 3]
    