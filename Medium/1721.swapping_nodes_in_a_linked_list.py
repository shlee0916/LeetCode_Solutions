'''
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = back = head

        for _ in range(1, k):
            front = front.next

        back_pointer = front
        while back_pointer.next:
            back_pointer = back_pointer.next
            back = back.next

        front.val, back.val = back.val, front.val

        return head


if __name__ == "__main__":
    ## Test helper
    def list2linked_list(arr: List[int]) -> ListNode:
        head = ListNode(arr[0])
        cur_node = head

        for val in arr[1:]:
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

        return head


    def linked_list2list(head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res
    ###############

    sol = Solution()

    test1_list = list2linked_list([1, 2, 3, 4, 5]) # ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test1 = sol.swapNodes(head = test1_list, k = 2)
    test1_res = linked_list2list(test1)
    assert test1_res == [1, 4, 3, 2, 5]

    test2_list = list2linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]) # ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
    test2 = sol.swapNodes(head = test2_list, k = 5)
    test2_res = linked_list2list(test2)
    assert test2_res == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
