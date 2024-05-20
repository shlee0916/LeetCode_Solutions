'''
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
'''

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        return sum(cost) - sum(cost[-3::-3])


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumCost(cost = [1, 2, 3])
    assert test1 == 5
    
    test2 = sol.minimumCost(cost = [6, 5, 7, 9, 2, 2])
    assert test2 == 23
    
    test3 = sol.minimumCost(cost = [5, 5])
    assert test3 == 10
    