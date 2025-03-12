'''
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/
'''

from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low = 1
        hi = 10 ** 7 + 1
        length = len(dist)

        while low < hi:
            speed = low + (hi - low) // 2

            expect_hour = dist[-1] / speed + sum(ceil(dist[i] / speed) for i in range(length - 1))

            if expect_hour > hour:
                low = speed + 1
            else:
                hi = speed

        return -1 if low == 10 ** 7 + 1 else low


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minSpeedOnTime(dist = [1, 3, 2], hour = 6)
    assert test1 == 1
    
    test2 = sol.minSpeedOnTime(dist = [1, 3, 2], hour = 2.7)
    assert test2 == 3
    
    test3 = sol.minSpeedOnTime(dist = [1, 3, 2], hour = 1.9)
    assert test3 == -1
    