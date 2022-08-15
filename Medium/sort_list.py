'''
https://leetcode.com/problems/sort-list/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        all_nodes = []
        
        while head:
            all_nodes.append(head)
            head = head.next
            
        all_nodes.sort(key = lambda x: x.val)
        
        new_node = all_nodes[0]
        for node in all_nodes[1:]:
            new_node.next = node
            new_node = new_node.next
            
        new_node.next = None
        
        return all_nodes[0]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test_list = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

    new_list = sol.sortList(test_list)
    sorted_list = []
    while new_list:
        sorted_list.append(new_list.val)
        new_list = new_list.next
        
    print(sorted_list)