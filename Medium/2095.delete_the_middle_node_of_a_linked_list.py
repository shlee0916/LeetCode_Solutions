'''
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head


if __name__ == "__main__":
    def print_list(head):
        while head:
            print(head.val, end = " ")
            head = head.next
        print()
    
    sol = Solution()

    test_list1 = ListNode(1)
    test_list1.next = ListNode(2)
    test_list1.next.next = ListNode(3)
    test_list1.next.next.next = ListNode(4)

    print_list(sol.deleteMiddle(test_list1))
