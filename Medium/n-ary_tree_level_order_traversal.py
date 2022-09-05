'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        que = [root]
        ans = []
        while que:
            level = []
            cur_level_len = len(que)
            
            for idx in range(cur_level_len):
                cur_node = que.pop(0)
                level.append(cur_node.val)
                print(cur_node.val)
                
                if cur_node.children is not None:
                    for ch in cur_node.children:
                        que.append(ch)

            ans.append(level)
            
        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.levelOrder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))