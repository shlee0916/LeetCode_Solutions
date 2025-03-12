'''
https://leetcode.com/problems/reorder-list/description/
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return []

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev_node, cur_node = None, slow.next
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node

            prev_node = cur_node
            cur_node = next_node
        slow.next = None

        res1, res2 = head, prev_node
        while res2:
            next_node = res1.next
            res1.next = res2

            res1 = res2
            res2 = next_node


if __name__ == "__main__":
    def node2list(head: Optional[ListNode]):
        values = []
        while head:
            values.append(head.val)
            head = head.next
            
        return values
    
    sol = Solution()
    
    test1_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol.reorderList(test1_list)
    test1 = node2list(test1_list)
    print(test1, [1, 4, 2, 3])
    assert test1 == [1, 4, 2, 3]
    
    test2_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol.reorderList(test2_list)
    test2 = node2list(test2_list)
    print(test2, [1, 5, 2, 4, 3])
    assert test2 == [1, 5, 2, 4, 3]
