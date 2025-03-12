'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0

        profits = [0] * (days + 1)
        max_profits = [0] * (days + 1)
        diff = [prices[idx + 1] - prices[idx] for idx in range(days - 1)]

        for day in range(days - 1):
            profits[day] = diff[day] + max(max_profits[day - 3], profits[day - 1])
            max_profits[day] = max(max_profits[day - 1], profits[day])

        return max_profits[-3]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxProfit([1, 2, 3, 0, 2])
    print(test1, 3)
    assert test1 == 3
    
    test2 = sol.maxProfit([1])
    print(test2, 0)
    assert test2 == 0
        