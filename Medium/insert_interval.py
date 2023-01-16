'''
https://leetcode.com/problems/insert-interval/description/
'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        idx = -1
        new_start = newInterval[0]
        new_end = newInterval[1]
        for idx, (start, end) in enumerate(intervals):
            if end < new_start:
                result.append([start, end])
            elif new_end < start:
                idx -= 1
                break
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        return result + [[new_start, new_end]] + intervals[idx + 1:]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.insert(intervals = [[1, 3], [6, 9]], newInterval = [2, 5])
    print(test1, [[1, 5], [6, 9]])
    assert test1 == [[1, 5], [6, 9]]

    test2 = sol.insert(intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8])
    print(test2, [[1, 2], [3, 10], [12, 16]])
    assert test2 == [[1, 2], [3, 10], [12, 16]]
