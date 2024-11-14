'''
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/?envType=daily-question&envId=2024-11-14
'''

from math import ceil

from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        while left < right:
            mid = (left + right) >> 1

            if sum(ceil(quantity / mid) for quantity in quantities) <= n:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimizedMaximum(n = 6, quantities = [11, 6])
    assert test1 == 3

    test2 = sol.minimizedMaximum(n = 7, quantities = [15, 10, 10])
    assert test2 == 5

    test3 = sol.minimizedMaximum(n = 1, quantities = [100000])
    assert test3 == 100000
    