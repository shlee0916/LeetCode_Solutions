'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        cur_node = head
        next_node = cur_node.next

        while next_node:
            if next_node.val == cur_node.val:
                cur_node.next = next_node.next
            else:
                cur_node = next_node
            next_node = next_node.next

        return head


if __name__ == "__main__":
    ############## Test Helper #############
    def linked2list(node: Optional[ListNode]):
        res = []

        while node:
            res.append(node.val)
            node = node.next
    
        return res
    #######################################
    
    sol = Solution()
    
    test1_list = ListNode(1, ListNode(1, ListNode(2)))
    test1 = sol.deleteDuplicates(test1_list)
    assert linked2list(test1) == [1, 2]
    
    test2_list = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3))))))
    test2 = sol.deleteDuplicates(test2_list)
    assert linked2list(test2) == [1, 2, 3]
    