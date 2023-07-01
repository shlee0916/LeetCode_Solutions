'''
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
'''

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices[:]

        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                ans[stack.pop()] -= price

            stack.append(idx)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.finalPrices(prices = [8, 4, 6, 2, 3])
    assert test1 == [4, 2, 4, 2, 3]

    test2 = sol.finalPrices(prices = [1, 2, 3, 4, 5])
    assert test2 == [1, 2, 3, 4, 5]
    
    test3 = sol.finalPrices(prices = [10, 1, 1, 6])
    assert test3 == [9, 0, 1, 6]
    