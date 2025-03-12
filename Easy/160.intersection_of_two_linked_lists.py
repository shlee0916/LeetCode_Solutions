'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
        

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        a_pointer = headA
        b_pointer = headB

        a_length = 1
        while a_pointer.next:
            a_pointer = a_pointer.next
            a_length += 1

        b_length = 1
        while b_pointer.next:
            b_pointer = b_pointer.next
            b_length += 1

        if a_pointer != b_pointer:
            return None

        else:
            long_list = headA if a_length > b_length else headB
            short_list = headA if long_list == headB else headB

            for _ in range(abs(a_length - b_length)):
                long_list = long_list.next

            while long_list != short_list:
                long_list = long_list.next
                short_list = short_list.next
            
            return long_list


if __name__ == "__main__":
    sol = Solution()
    
    test1_lista = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    test1_listb = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))
    test1 = sol.getIntersectionNode(test1_lista, test1_listb)
    # assert test1.val == 8
    
    test2_lista = ListNode(2, ListNode(6, ListNode(4)))
    test2_listb = ListNode(1, ListNode(5))
    test2 = sol.getIntersectionNode(test2_lista, test2_listb)
    # assert test2 == None
    
    # There is different test method..
    