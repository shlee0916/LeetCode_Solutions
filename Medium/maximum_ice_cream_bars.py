'''
https://leetcode.com/problems/maximum-ice-cream-bars/description/
'''

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        cur_money = coins
        res = 0
        for cost in costs:
            if cur_money - cost >= 0:
                cur_money -= cost
                res += 1
            else:
                break

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxIceCream(costs = [1, 3, 2, 4, 1], coins = 7)
    print(test1, 4)
    assert test1 == 4

    test2 = sol.maxIceCream(costs = [10, 6, 8, 7, 7, 8], coins = 5)
    print(test2, 0)
    assert test2 == 0

    test3 = sol.maxIceCream(costs = [1, 6, 3, 1, 2, 5], coins = 20)
    print(test3, 6)
    assert test3 == 6
    