'''
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2024-09-06
'''

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        num_set = set(nums)
        cur_node = dummy
        next_node = dummy.next
        while next_node:
            if next_node.val not in num_set:
                cur_node.next = next_node
                cur_node = cur_node.next
            
            next_node = next_node.next

        cur_node.next = None

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

    test1_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test1 = sol.modifiedList(nums = [1, 2, 3], head = test1_list)
    assert linked2list(test1) == [4, 5]

    test2_list = ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2))))))
    test2 = sol.modifiedList(nums = [1], head = test2_list)
    assert linked2list(test2) == [2, 2, 2]

    test3_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    test3 = sol.modifiedList(nums = [5], head = test3_list)
    assert linked2list(test3) == [1, 2, 3, 4]
