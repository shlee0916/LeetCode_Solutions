'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
            
        cur.next = None
            
        return head.next
    
    
if __name__ == "__main__":
    sol = Solution()
    
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    print(sol.mergeTwoLists(list1, list2))