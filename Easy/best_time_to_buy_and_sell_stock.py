'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        
        for price in prices[1:]:
            if buy > price:
                buy = min(price, buy)
            else:
                profit = max(price - buy, profit)
                
        return profit
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)