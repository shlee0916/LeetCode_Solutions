'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
'''

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            day = 1
            cur = 0

            for weight in weights:
                if cur + weight > mid:
                    day += 1
                    cur = 0
                cur += weight

            if day > days:
                left = mid + 1
            else:
                right = mid
        
        return left


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.shipWithinDays(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5)
    print(test1, 15)
    assert test1 == 15

    test2 = sol.shipWithinDays(weights = [3, 2, 2, 4, 1, 4], days = 3)
    print(test2, 6)
    assert test2 == 6

    test3 = sol.shipWithinDays(weights = [1, 2, 3, 1, 1], days = 4)
    print(test3, 3)
    assert test3 == 3
    