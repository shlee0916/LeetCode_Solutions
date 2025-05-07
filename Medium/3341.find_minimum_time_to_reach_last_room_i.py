'''
https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/?envType=daily-question&envId=2025-05-07
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        row_limit = len(moveTime)
        col_limit = len(moveTime[0])

        dp = [[float("inf")] * col_limit for _ in range(row_limit)]
        heap = [(0, (0, 0))]

        moveTime[0][0] = 0
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while heap:
            cur_time, (cur_row, cur_col) = heappop(heap)

            if cur_time >= dp[cur_row][cur_col]:
                continue

            if (cur_row, cur_col) == (row_limit - 1, col_limit - 1):
                return cur_time

            dp[cur_row][cur_col] = cur_time

            for dr, dc in dirs:
                next_row = cur_row + dr
                next_col = cur_col + dc

                if 0 <= next_row < row_limit and 0 <= next_col < col_limit and dp[next_row][next_col] == float("inf"):
                    next_time = max(moveTime[next_row][next_col], cur_time) + 1
                    heappush(heap, (next_time, (next_row, next_col)))

        return -1
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minTimeToReach(moveTime = [[0, 4], [4, 4]])
    assert test1 == 6

    test2 = sol.minTimeToReach(moveTime = [[0, 0, 0], [0, 0, 0]])
    assert test2 == 3

    test3 = sol.minTimeToReach(moveTime = [[0, 1], [1, 2]])
    assert test3 == 3
