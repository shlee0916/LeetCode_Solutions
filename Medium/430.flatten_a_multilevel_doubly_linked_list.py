'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
'''

from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return

        stack = [head]
        prev = Node(0) # Start with dummy
        while stack:
            cur_node = stack.pop()
            cur_node.prev = prev
            prev.next = cur_node
            prev = cur_node

            if cur_node.next:
                stack.append(cur_node.next)
            if cur_node.child:
                stack.append(cur_node.child)
                cur_node.child = None

        head.prev = None

        return head
                

if __name__ == "__main__":
    # Test Helper
    def print_list(head: Node) -> List[int]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        return vals
    ##############

    sol = Solution()

    test1_head = Node(1)
    test1_head.next = Node(2, test1_head)
    test1_head.child = Node(3)
    test1 = sol.flatten(test1_head)
    print(print_list(test1))
    assert print_list(test1) == [1, 3, 2]
