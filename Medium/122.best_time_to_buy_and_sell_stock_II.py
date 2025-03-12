'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = -float("inf"), 0
        for price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            cur_hold = max(prev_hold, prev_not_hold - price)
            cur_not_hold = max(prev_not_hold, prev_hold + price)

        return cur_not_hold


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxProfit(prices = [7, 1, 5, 3, 6, 4])
    print(test1, 7)
    assert test1 == 7

    test2 = sol.maxProfit(prices = [1, 2, 3, 4, 5])
    print(test2, 4)
    assert test2 == 4

    test3 = sol.maxProfit(prices = [7, 6, 4, 3, 1])
    print(test3, 0)
    assert test3 == 0
