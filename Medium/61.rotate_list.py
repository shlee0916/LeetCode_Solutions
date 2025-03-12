'''
https://leetcode.com/problems/rotate-list/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            length = 1
        else:
            return

        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            length += 1

        k %= length
        if k == 0:
            new_head = head
        else:
            cur_node.next = head
            new_head = head
            for _ in range(length - k):
                prev = new_head
                new_head = new_head.next
            prev.next = None

        return new_head


if __name__ == "__main__":
    def print_list(head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res

    sol = Solution()

    test1_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test1 = sol.rotateRight(head = test1_list, k = 2)
    test1_res = print_list(test1)
    print([4, 5, 1, 2, 3], test1_res)
    assert test1_res == [4, 5, 1, 2, 3]

    test2_list = ListNode(0, ListNode(1, ListNode(2)))
    test2 = sol.rotateRight(head = test2_list, k = 4)
    test2_res = print_list(test2)
    print([2, 0, 1], test2_res)
    assert test2_res == [2, 0, 1]
