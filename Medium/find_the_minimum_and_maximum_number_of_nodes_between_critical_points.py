'''
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/?envType=daily-question&envId=2024-07-05
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return [-1, -1]

        pre_node = head
        cur_node = head.next

        critical_point = []
        idx = 2
        while cur_node.next is not None:
            if pre_node.val < cur_node.val and cur_node.next.val < cur_node.val:
                critical_point.append(idx)
                
            if pre_node.val > cur_node.val and cur_node.next.val > cur_node.val:
                critical_point.append(idx)

            idx += 1
            pre_node = cur_node
            cur_node = cur_node.next

        ans = [-1, -1]
        if len(critical_point) >= 2:
            ans[0] = min(critical_point[idx] - critical_point[idx - 1] for idx in range(len(critical_point) - 1,  0, -1))
            ans[1] = max(critical_point) - min(critical_point)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1_list = ListNode(3, ListNode(1))
    test1 = sol.nodesBetweenCriticalPoints(test1_list)
    assert test1 == [-1, -1]

    test2_list = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
    test2 = sol.nodesBetweenCriticalPoints(test2_list)
    assert test2 == [1, 3]

    test3_list = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))
    test3 = sol.nodesBetweenCriticalPoints(test3_list)
    assert test3 == [3, 3]
    