'''
https://leetcode.com/problems/remove-nodes-from-linked-list/description/
'''

from typing import Optional
from math import inf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float(inf))
        stack = [dummy]
        
        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()

            stack[-1].next = head
            stack.append(head)
            head = head.next

        return dummy.next


if __name__ == "__main__":
    ##### Test Helper
    def linked2list(head: ListNode):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
            
        return vals
    #################
    
    sol = Solution()
    
    test1_list = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    test1 = sol.removeNodes(test1_list)
    assert linked2list(test1) == [13, 8]
    
    test2_list = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
    test2 = sol.removeNodes(test2_list)
    assert linked2list(test2) == [1, 1, 1, 1]
    