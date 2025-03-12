'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        
        que = [root]
        
        while que:
            cur_level = []
            cur_level_len = len(que)
            for _ in range(cur_level_len):
                cur_node = que.pop(0)
                cur_level.append(cur_node)
                if cur_node.left is not None:
                    que.append(cur_node.left)
                    que.append(cur_node.right)
            
            level_head = cur_level.pop(0)
            while cur_level:
                cur_node = cur_level.pop(0)
                level_head.next = cur_node
                level_head = level_head.next
            level_head.next = None
            
        return root
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    
    print(sol.connect(test_tree))
    
    
    # Test print
    que = [test_tree]
    
    while que:
        cur_node = que.pop(0)
        if cur_node.left is not None:
            que.append(cur_node.left)
        
        while cur_node is not None:
            print(cur_node.val, end = " ")
            cur_node = cur_node.next
        
        print("#")
        