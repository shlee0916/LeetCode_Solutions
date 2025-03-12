'''
https://leetcode.com/problems/remove-linked-list-elements/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return

        dummy = ListNode(-1)
        dummy.next = head

        cur_node = dummy
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
            
        return dummy.next
        
        
if __name__ == "__main__":
    # Test Helper
    def print_list(head: ListNode) -> List[int]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        return vals
    ##############
    sol = Solution()
    
    test1_list = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    test1 = sol.removeElements(test1_list, 6)
    assert print_list(test1) == [1, 2, 3, 4, 5]

    test2_list = None
    test2 = sol.removeElements(test2_list, 1)
    assert test2 == None
    
    test3_list = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    test3 = sol.removeElements(test3_list, 7)
    assert test3 == None
    