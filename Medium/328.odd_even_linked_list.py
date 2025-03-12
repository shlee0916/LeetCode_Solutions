'''
https://leetcode.com/problems/odd-even-linked-list/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        odd_head = head
        even_head = head.next
        new_even_head = even_head
        while  even_head and even_head.next:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next

            even_head.next = even_head.next.next
            even_head = even_head.next

        odd_head.next = new_even_head

        return head


if __name__ == "__main__":
    ### Test Helper ###
    def list2link(nums: List[int]):
        first = ListNode(nums[0])

        cur_node = first
        for num in nums[1:]:
            cur_node.next = ListNode(num)
            cur_node = cur_node.next

        return first

    
    def link2list(head: Optional[ListNode]):
        vals = []

        while head:
            vals.append(head.val)
            head = head.next
        
        return vals
    
    ### ----------- ###

    sol = Solution()

    test1_list = list2link([1, 2, 3, 4, 5])
    test1 = sol.oddEvenList(test1_list)
    test1_res = link2list(test1)
    print(test1_res, [1, 3, 5, 2, 4])
    assert test1_res == [1, 3, 5, 2, 4]

    test2_list = list2link([2, 1, 3, 5, 6, 4, 7])
    test2 = sol.oddEvenList(test2_list)
    test2_res = link2list(test2)
    print(test2_res, [2, 3, 6, 7, 1, 5, 4])
    assert test2_res == [2, 3, 6, 7, 1, 5, 4]
