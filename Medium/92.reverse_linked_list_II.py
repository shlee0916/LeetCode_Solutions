'''
https://leetcode.com/problems/reverse-linked-list-ii/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        cnt = 1
        cur = head
        left_node = None
        right_node = None
        stack = []
        while cur:
            if left - 1 == cnt:
                left_node = cur
            if right + 1 == cnt:
                right_node = cur
            if cnt >= left and cnt <= right:
                stack.append(cur)
            
            cnt += 1
            cur = cur.next
            
        while stack:
            cur_node = stack.pop()
            cur_node.next = None
            if left_node:
                left_node.next = cur_node
                left_node = left_node.next
            else:
                head = cur_node
                left_node = cur_node
            
        left_node.next = right_node
            
        return head
    

if __name__ == "__main__":
    from copy import deepcopy
    sol = Solution()
    
    test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_list = sol.reverseBetween(deepcopy(test_list), 2, 4)
    
    while test_list:
        print(test_list.val, end = " ")
        test_list = test_list.next
    
    print()
    while reversed_list:
        print(reversed_list.val, end = " ")
        reversed_list = reversed_list.next
    