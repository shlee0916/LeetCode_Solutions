'''
https://leetcode.com/problems/palindrome-linked-list/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        all_values = []
        while head:
            all_values.append(head.val)
            head = head.next
    
        mid_point = len(all_values) // 2
        
        return all_values[:mid_point] == all_values[mid_point:][::-1] if len(all_values) % 2 == 0 else all_values[:mid_point + 1] == all_values[mid_point:][::-1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))