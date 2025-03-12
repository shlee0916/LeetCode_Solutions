'''
https://leetcode.com/problems/coin-change/description/
'''

import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coin_cnts = [0] + [math.inf] * amount
        
        for idx in range(1, amount + 1):
            for coin in coins:
                if amount >= coin:
                    coin_cnts[idx] = min(coin_cnts[idx], coin_cnts[idx - coin] + 1)
                else:
                    break

        return coin_cnts[amount] if coin_cnts[amount] != math.inf else -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.coinChange(coins = [1, 2, 5], amount = 11)
    print(test1, 3)
    assert test1 == 3

    test2 = sol.coinChange(coins = [2], amount = 3)
    print(test2, -1)
    assert test2 == -1

    test3 = sol.coinChange(coins = [1], amount = 0)
    print(test3, 0)
    assert test3 == 0
