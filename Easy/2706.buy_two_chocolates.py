'''
https://leetcode.com/problems/buy-two-chocolates/description/?envType=daily-question&envId=2023-12-20
'''

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        return (money - sum(prices[:2])) if sum(prices[:2]) <= money else money
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.buyChoco(prices = [1, 2, 2], money = 3)
    assert test1 == 0
    
    test2 = sol.buyChoco(prices = [3, 2, 3], money = 3)
    assert test2 == 3
    