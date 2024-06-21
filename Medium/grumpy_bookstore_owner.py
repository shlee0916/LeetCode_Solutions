'''
https://leetcode.com/problems/grumpy-bookstore-owner/?envType=daily-question&envId=2024-06-21
'''

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        for idx in range(len(customers)):
            if grumpy[idx] == 0:
                satisfied += customers[idx]
                customers[idx] = 0

        max_sat = 0
        cur_sat = 0
        for idx, sat in enumerate(customers):
            cur_sat += sat
            if idx >= minutes:
                cur_sat -= customers[idx - minutes]

            max_sat = max(max_sat, cur_sat)

        return satisfied + max_sat
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxSatisfied(customers = [1, 0, 1, 2, 1, 1, 7, 5], grumpy = [0, 1, 0, 1, 0, 1, 0, 1], minutes = 3)
    assert test1 == 16

    test2 = sol.maxSatisfied(customers = [1], grumpy = [0], minutes = 1)
    assert test2 == 1
    