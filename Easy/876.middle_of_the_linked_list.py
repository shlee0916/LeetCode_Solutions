'''
https://leetcode.com/problems/middle-of-the-linked-list/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
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
    
    
    sol = Solution()

    test1_link = list2link([1, 2, 3, 4, 5])
    test1 = sol.middleNode(test1_link)
    test1_res = link2list(test1)
    print(test1_res, [3, 4, 5])
    assert test1_res == [3, 4, 5]
    
    test2_link = list2link([1, 2, 3, 4, 5, 6])
    test2 = sol.middleNode(test2_link)
    test2_res = link2list(test2)
    print(test2_res, [4, 5, 6])
    assert test2_res == [4, 5, 6]
    