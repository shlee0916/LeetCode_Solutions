'''
https://leetcode.com/problems/minimum-time-to-repair-cars/?envType=daily-question&envId=2025-03-16
'''

from math import isqrt

from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = max(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2

            if sum(isqrt(mid // r) for r in ranks) < cars:
                left = mid + 1
            else:
                right = mid

        return left
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.repairCars(ranks = [4, 2, 3, 1], cars = 10)
    assert test1 == 16

    test2 = sol.repairCars(ranks = [5, 1, 8], cars = 6)
    assert test2 == 16
    