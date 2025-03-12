'''
https://leetcode.com/problems/binary-tree-paths/
'''
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return None
        
        que = [(root, str(root.val))]
        ans = []
        
        while que:
            cur_node, cur_path = que.pop()
            
            if not any([cur_node.left, cur_node.right]):
                ans.append(cur_path)
                
            else:
                if cur_node.left is not None:
                    que.append((cur_node.left, cur_path + "->" + str(cur_node.left.val)))
                if cur_node.right is not None:
                    que.append((cur_node.right, cur_path + "->" + str(cur_node.right.val)))  
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))
    print(sol.binaryTreePaths(test_tree))

    