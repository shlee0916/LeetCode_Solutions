'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Brute force
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        ori_head = head
        end_node = head
        
        node_list = []
        while end_node:
            node_list.append(end_node)
            end_node = end_node.next
            
        if len(node_list) == n:
            node_list[0].next = None
            if len(node_list) == 1:
                head = None
            else:
                head = node_list[1]
        elif n == 1:
            node_list[-2].next = None
        else:  
            node_list[-n - 1].next = node_list[-n + 1]
        
        return head

    # Two pointer
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f_head, r_head = head, head
    
        for _ in range(n):
            f_head = f_head.next
            
        if not f_head:
            return head.next
        
        while f_head.next:
            f_head = f_head.next
            r_head = r_head.next
            
        r_head.next = r_head.next.next
        
        return head


if __name__ == "__main__":
    sol = Solution()

    test_list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test_list2 = ListNode(1, ListNode(2))
    test_list3 = ListNode(1)

    test_list1 = sol.removeNthFromEnd(test_list1, 2)
    test_list2 = sol.removeNthFromEnd(test_list2, 1)
    test_list3 = sol.removeNthFromEnd(test_list3, 1)

    def print_node(list):
        while list:
            print(list.val, end = "")
            list = list.next
        
        print()

    print_node(test_list1)
    print_node(test_list2)
    print_node(test_list3)
