'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        dummy = ListNode(-1, head)
        prev_node = dummy
        cur_node = prev_node.next

        while cur_node and cur_node.next:
            if cur_node.val == cur_node.next.val:
                while cur_node and cur_node.next and cur_node.val == cur_node.next.val:
                    cur_node = cur_node.next

                cur_node = cur_node.next
                prev_node.next = cur_node
            else:
                prev_node = cur_node
                cur_node = cur_node.next

        return dummy.next
    

if __name__ == "__main__":
    ### Test helper
    def linked2list(head: ListNode) -> List[int]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        return lst
    ###################################

    sol = Solution()

    test1_list = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    test1 = sol.deleteDuplicates(test1_list)
    assert linked2list(test1) == [1, 2, 5]

    test2_list = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    test2 = sol.deleteDuplicates(test2_list)
    assert linked2list(test2) == [2, 3]
