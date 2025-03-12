'''
https://leetcode.com/problems/spiral-matrix-iv/?envType=daily-question&envId=2024-09-09
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        new_mat = [[-1] * n for _ in range(m)]

        dx = 0
        dy = 1
        cur_x, cur_y = 0, 0
        while head:
            new_mat[cur_x][cur_y] = head.val

            if (cur_x + dx < 0 or
                cur_x + dx >= m or
                cur_y + dy < 0 or
                cur_y + dy >= n or
                new_mat[cur_x + dx][cur_y + dy] != -1):
                dy, dx = -dx, dy

            cur_x += dx
            cur_y += dy

            head = head.next

        return new_mat


if __name__ == "__main__":
    sol = Solution()

    test1_list = ListNode(3, ListNode(0 ,ListNode(2, ListNode(6, ListNode(8, ListNode(1, ListNode(7, ListNode(9, ListNode(4, ListNode(2, ListNode(5, ListNode(5, ListNode(0)))))))))))))
    test1 = sol.spiralMatrix(m = 3, n = 5, head = test1_list)
    assert test1 == [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]

    test2_list = ListNode(0, ListNode(1, ListNode(2)))
    test2 = sol.spiralMatrix(m = 1, n = 4, head = test2_list)
    assert test2 == [[0, 1, 2, -1]]
    