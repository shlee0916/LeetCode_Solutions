'''
https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description/?envType=daily-question&envId=2025-05-08
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        row_limit = len(moveTime)
        col_limit = len(moveTime[0])

        visit = {(0, 0)}
        heap = [(0, 0, (0, 0))]
        moveTime[0][0] = 0
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while heap:
            cur_time, cur_mv_cnt, (cur_row, cur_col) = heappop(heap)

            if (cur_row, cur_col) == (row_limit - 1, col_limit - 1):
                return cur_time

            for dr, dc in dirs:
                next_row = cur_row + dr
                next_col = cur_col + dc

                if 0 <= next_row < row_limit and 0 <= next_col < col_limit and \
                   (next_row, next_col) not in visit:
                    visit.add((next_row, next_col))
                    next_time = max(cur_time, moveTime[next_row][next_col])
                    if cur_mv_cnt % 2 == 0:
                        next_time += 1
                    else:
                        next_time += 2
                    
                    heappush(heap, (next_time, cur_mv_cnt + 1, (next_row, next_col)))

        return -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minTimeToReach(moveTime = [[0, 4], [4, 4]])
    assert test1 == 7

    test2 = sol.minTimeToReach(moveTime = [[0, 0, 0, 0], [0, 0, 0, 0]])
    assert test2 == 6
    