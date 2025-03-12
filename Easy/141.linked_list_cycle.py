'''
https://leetcode.com/problems/linked-list-cycle/
'''
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = []
        
        while head:
            if head not in visit:
                visit.append(head)
            else:
                return True
            
            head = head.next
            
        return False


if __name__ == "__main__":
    sol = Solution()

    head1 = ListNode(3)
    head1.next = ListNode(2)
    head1.next.next = ListNode(0)
    head1.next.next.next = ListNode(-4)
    head1.next.next.next.next = head1.next

    head2 = ListNode(1)

    print(sol.hasCycle(head1))
    print(sol.hasCycle(head2))