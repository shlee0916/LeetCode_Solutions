'''
https://leetcode.com/problems/remove-covered-intervals/description/
'''

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_inter = sorted(intervals, key = lambda x: (x[0], -x[1]))
        
        cur_right_bound = 0
        cnt = 0
        for _, right_bound in sorted_inter:
            if right_bound > cur_right_bound:
                cnt += 1
                cur_right_bound = right_bound

        return cnt


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.removeCoveredIntervals(intervals = [[1, 4], [3, 6], [2, 8]])
    assert test1 == 2

    test2 = sol.removeCoveredIntervals(intervals = [[1, 4], [2, 3]])
    assert test2 == 1
    