'''
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/?envType=daily-question&envId=2024-05-07
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            head = ListNode(0, head)
        
        node = head
        while node:
            node.val = node.val * 2 % 10
            if node.next and node.next.val >= 5:
                node.val += 1

            node = node.next

        return head
        

if __name__ == "__main__":
    ############## Test Helper #############
    def linked2list(node: Optional[ListNode]):
        res = []

        while node:
            res.append(node.val)
            node = node.next
    
        return res
    ########################################
    sol = Solution()

    test1_list = ListNode(1, ListNode(8, ListNode(9)))
    test1 = sol.doubleIt(test1_list)
    assert linked2list(test1) == [3, 7, 8]

    test2_list = ListNode(9, ListNode(9, ListNode(9)))
    test2 = sol.doubleIt(test2_list)
    assert linked2list(test2) == [1, 9, 9, 8]
