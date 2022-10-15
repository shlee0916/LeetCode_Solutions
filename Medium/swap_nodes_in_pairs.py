'''
https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur            
            prev, cur = cur, cur.next
            
        return dummy.next
    
    
if __name__ == "__main__":
    def print_list(head):
        while head:
            print(head.val, end = " ")
            head = head.next
            
        print()
    
    sol = Solution()
    
    test_list = ListNode(1)
    test_list.next = ListNode(2)
    test_list.next.next = ListNode(3)
    test_list.next.next.next = ListNode(4)
    
    print_list(test_list)
    
    print_list(sol.swapPairs(test_list))