'''
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/?envType=daily-question&envId=2024-09-10
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            
            return a

        cur_node = head
        next_node = head.next
        while next_node:
            new_node = ListNode(gcd(cur_node.val, next_node.val))

            cur_node.next = new_node
            new_node.next = next_node

            cur_node = next_node
            next_node = next_node.next

        return head


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

    test1_list = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    test1 = sol.insertGreatestCommonDivisors(test1_list)
    assert linked2list(test1) == [18 ,6, 6, 2, 10, 1, 3]

    test2_list = ListNode(7)
    test2 = sol.insertGreatestCommonDivisors(test2_list)
    assert linked2list(test2) == [7]
    