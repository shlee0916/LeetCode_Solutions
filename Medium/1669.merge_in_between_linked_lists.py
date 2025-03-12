'''
https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = None
        tail = list1

        for idx in range(b):
            if idx == a - 1:
                head = tail
            tail = tail.next
        
        head.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = tail.next
        tail.next = None

        return list1


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

    test1_list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
    test1_list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    test1 = sol.mergeInBetween(list1 = test1_list1, a = 3, b = 4, list2 = test1_list2)
    assert linked2list(test1) == [10, 1, 13, 1000000, 1000001, 1000002, 5]

    test2_list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    test2_list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004)))))
    test2 = sol.mergeInBetween(list1 = test2_list1, a = 2, b = 5, list2 = test2_list2)
    assert linked2list(test2) == [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
    