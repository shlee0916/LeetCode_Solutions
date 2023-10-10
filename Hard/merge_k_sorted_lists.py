'''
https://leetcode.com/problems/merge-k-sorted-lists/description/
'''

from heapq import heappush, heappop

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list = []

        for head in lists:
            while head:
                heappush(new_list, head.val)
                head = head.next

        dummy = head = ListNode()
        while new_list:
            head.next = ListNode(heappop(new_list))
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

    test1_list1 = ListNode(1, ListNode(4, ListNode(5)))
    test1_list2 = ListNode(1, ListNode(3, ListNode(4)))
    test1_list3 = ListNode(2, ListNode(6))
    test1_lists = [test1_list1, test1_list2, test1_list3]
    test1 = sol.mergeKLists(test1_lists)
    assert linked2list(test1) == [1, 1, 2, 3, 4, 4, 5, 6]

    test2_lists = []
    test2 = sol.mergeKLists(test2_lists)
    assert test2 == None

    test3_lists = [ListNode()]
    test3 = sol.mergeKLists(test3_lists)
    assert linked2list(test3) == [0]
