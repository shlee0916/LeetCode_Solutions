'''
https://leetcode.com/problems/coin-change-ii/description/?envType=daily-question&envId=2023-09-18
'''

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount + 1)

        for coin in coins:
            for target in range(1, amount + 1):
                if target >= coin:
                    dp[target] += dp[target - coin]

        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.change(amount = 5, coins = [1, 2, 5])
    assert test1 == 4
    
    test2 = sol.change(amount = 3, coins = [2])
    assert test2 == 0
    
    test3 = sol.change(amount = 10, coins = [10])
    assert test3 == 1
    