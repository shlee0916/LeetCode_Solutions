'''
https://leetcode.com/problems/partition-list/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode(0)
        right_head = ListNode(0)

        left = left_head
        right = right_head
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        right.next = None
        left.next = right_head.next

        return left_head.next
    
    
if __name__ == "__main__":
    def print_list(head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res
    
    sol = Solution()
    
    test1_list = ListNode(1, ListNode(4 ,ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    test1 = sol.partition(test1_list, 3)
    test1_res = print_list(test1)
    print(test1_res, [1, 2, 2, 4, 3, 5])
    assert test1_res == [1, 2, 2, 4, 3, 5]
    
    test2_list = ListNode(2, ListNode(1))
    test2 = sol.partition(test2_list, 2)
    test2_res = print_list(test2)
    print(test2_res, [1, 2])
    assert test2_res == [1, 2]
    