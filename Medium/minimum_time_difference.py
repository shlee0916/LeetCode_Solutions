'''
https://leetcode.com/problems/minimum-time-difference/?envType=daily-question&envId=2024-09-22
'''

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_time = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        sorted_time.append(sorted_time[0] + 60 * 24)

        return min((t2 - t1) for t1, t2 in zip(sorted_time, sorted_time[1:]))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findMinDifference(timePoints = ["23:59", "00:00"])
    assert test1 == 1

    test2 = sol.findMinDifference(timePoints = ["00:00", "23:59", "00:00"])
    assert test2 == 0
    