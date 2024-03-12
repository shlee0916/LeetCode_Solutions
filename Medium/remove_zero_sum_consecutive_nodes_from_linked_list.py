'''
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        prefix_map = {}

        while head:
            prefix += head.val
            prefix_map[prefix] = head
            head = head.next

        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            if prefix in prefix_map:
                head.next = prefix_map[prefix].next

            head = head.next

        return dummy.next


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

    test1_list = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
    test1 = sol.removeZeroSumSublists(test1_list)
    assert linked2list(test1) == [3, 1]

    test2_list = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(4)))))
    test2 = sol.removeZeroSumSublists(test2_list)
    assert linked2list(test2) == [1, 2, 4]

    test3_list = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))
    test3 = sol.removeZeroSumSublists(test3_list)
    assert linked2list(test3) == [1]
    