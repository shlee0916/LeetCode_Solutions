'''
https://leetcode.com/problems/merge-nodes-in-between-zeros/?envType=daily-question&envId=2024-07-04
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        new_node = dummy

        cur_node = head.next
        cur_sum = 0

        while cur_node is not None:
            if cur_node.val == 0:
                new_node.next = ListNode(cur_sum)
                cur_sum = 0
                new_node = new_node.next
            else:
                cur_sum += cur_node.val
            
            cur_node = cur_node.next
        
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

    test1_list = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
    test1 = sol.mergeNodes(test1_list)
    assert linked2list(test1) == [4, 11]

    test2_list = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
    test2 = sol.mergeNodes(test2_list)
    assert linked2list(test2) == [1, 3, 4]
