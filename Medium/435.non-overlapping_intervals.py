'''
https://leetcode.com/problems/non-overlapping-intervals/description/
'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = -float("inf")
        remove_cnt = 0

        for new_start, new_end in sorted(intervals, key = lambda ele: ele[1]):
            if new_start >= end:
                end = new_end
            else:
                remove_cnt += 1

        return remove_cnt


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.eraseOverlapIntervals(intervals = [[1, 2], [2, 3], [3, 4], [1, 3]])
    assert test1 == 1
    
    test2 = sol.eraseOverlapIntervals(intervals = [[1, 2], [1, 2], [1, 2]])
    assert test2 == 2
    
    test3 = sol.eraseOverlapIntervals(intervals = [[1, 2], [2, 3]])
    assert test3 == 0
    