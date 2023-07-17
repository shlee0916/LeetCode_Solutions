'''
https://leetcode.com/problems/add-two-numbers-ii/description/
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []

        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next

        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while l1_stack or l2_stack or carry:
            l1_val = l1_stack.pop() if l1_stack else 0
            l2_val = l2_stack.pop() if l2_stack else 0

            carry, new_val = divmod(l1_val + l2_val + carry, 10)

            new_node = ListNode(new_val)
            new_node.next = head
            head = new_node

        return head


if __name__ == "__main__":
    ### Test helper ###
    def linked2list(head: ListNode):
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
        return vals
    ###################
    
    sol = Solution()
    
    test1_list1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    test1_list2 = ListNode(5, ListNode(6, ListNode(4)))
    test1_res = sol.addTwoNumbers(test1_list1, test1_list2)
    assert linked2list(test1_res) == [7, 8, 0, 7]
    
    test2_list1 = ListNode(2, ListNode(4, ListNode(3)))
    test2_list2 = ListNode(5, ListNode(6, ListNode(4)))
    test2_res = sol.addTwoNumbers(test2_list1, test2_list2)
    assert linked2list(test2_res) == [8, 0, 7]
    
    test3_list1 = ListNode(0)
    test3_list2 = ListNode(0)
    test3_res = sol.addTwoNumbers(test3_list1, test3_list2)
    assert linked2list(test3_res) == [0]
    