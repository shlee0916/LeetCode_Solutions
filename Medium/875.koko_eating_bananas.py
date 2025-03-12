'''
https://leetcode.com/problems/koko-eating-bananas/description/
'''

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if sum(math.ceil(pile / mid) for pile in piles) > h:
                left = mid + 1
            else:
                right = mid

        return left
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minEatingSpeed(piles = [3, 6, 7, 11], h = 8)
    print(test1, 4)
    assert test1 == 4

    test2 = sol.minEatingSpeed(piles = [30, 11, 23, 4, 20], h = 5)
    print(test2, 30)
    assert test2 == 30

    test3 = sol.minEatingSpeed(piles = [30, 11, 23, 4, 20], h = 6)
    print(test3, 23)
    assert test3 == 23
