'''
https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        before_group = dummy
        
        dummy.next = head
        left = head
        right = head

        count = 0
        while right and count < k:
            right = right.next
            count += 1

            if count == k:
                cur = left
                prev = right
                for _ in range(k):
                    cur.next, cur, prev = prev, cur.next, cur

                before_group.next, before_group, left = prev, left, right

                count = 0

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
    test1 = sol.reverseKGroup(head = test1_list, k = 2)
    assert linked2list(test1) == [2, 1, 4, 3, 5]

    test2_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test2 = sol.reverseKGroup(head = test2_list, k = 3)
    assert linked2list(test2) == [3, 2, 1, 4, 5]
