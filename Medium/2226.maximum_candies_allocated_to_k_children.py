'''
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14
'''

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        min_candy = 0
        max_candy = max(candies)

        while min_candy < max_candy:
            mid = (min_candy + max_candy + 1) // 2

            if k > sum(pile // mid for pile in candies):
                max_candy = mid - 1
            else:
                min_candy = mid

        return min_candy


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumCandies(candies = [5, 8, 6], k = 3)
    assert test1 == 5

    test2 = sol.maximumCandies(candies = [2, 5], k = 11)
    assert test2 == 0
    