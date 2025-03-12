'''
https://leetcode.com/problems/add-two-numbers/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
            
        new_num = int("".join(num1[::-1])) + int("".join(num2[::-1]))
        new_num = [num for num in str(new_num)]
        
        header = ListNode(val = int(new_num.pop()))
        cur_node = header
        while new_num:
            cur_node.next = ListNode(val = int(new_num.pop()))
            cur_node = cur_node.next
            
        return header

        
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))