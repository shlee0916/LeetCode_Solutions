'''
https://leetcode.com/problems/linked-list-cycle-ii/description/
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow, fast = slow.next, fast.next

                return slow

        return None


if __name__ == "__main__":
    sol = Solution()

    test1_list = ListNode(3)
    test1_list.next = ListNode(2)
    test1_list.next.next = ListNode(0)
    test1_list.next.next.next = ListNode(-4)
    test1_list.next.next.next.next = test1_list.next

    test1 = sol.detectCycle(test1_list)
    print(test1, test1_list.next)
    assert test1 == test1_list.next


    test2_list = ListNode(1)
    test2_list.next = ListNode(2)
    test2_list.next.next = test2_list

    test2 = sol.detectCycle(test2_list)
    print(test2, test2_list)
    assert test2 == test2_list

    
    test3_list = ListNode(1)

    test3 = sol.detectCycle(test3_list)
    print(test3, None)
    assert test3 == None
    