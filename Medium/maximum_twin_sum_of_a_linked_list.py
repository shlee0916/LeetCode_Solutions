'''
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid, end = head, head
        res = 0

        while end and end.next:
            end = end.next.next
            mid = mid.next

        cur_node = mid
        pre_node = None
        while cur_node:
            cur_node.next, pre_node, cur_node = pre_node, cur_node, cur_node.next
        
        while pre_node:
            res = max(res, head.val + pre_node.val)
            head = head.next
            pre_node = pre_node.next

        return res
    

if __name__ == "__main__":
    ## Test helper
    def list2linked_list(arr: List[int]) -> ListNode:
        head = ListNode(arr[0])
        cur_node = head

        for val in arr[1:]:
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

        return head
    ###############

    sol = Solution()

    test1_list = list2linked_list([5, 4, 2, 1])
    test1 = sol.pairSum(test1_list)
    assert test1 == 6

    test2_list = list2linked_list([4, 2, 2, 3])
    test2 = sol.pairSum(test2_list)
    assert test2 == 7

    test3_list = list2linked_list([1, 100000])
    test3 = sol.pairSum(test3_list)
    assert test3 == 100001
