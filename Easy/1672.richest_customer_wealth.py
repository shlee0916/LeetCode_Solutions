'''
https://leetcode.com/problems/richest-customer-wealth/description/
'''

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumWealth(accounts = [[1, 2, 3], [3, 2, 1]])
    assert test1 == 6
    
    test2 = sol.maximumWealth(accounts = [[1, 5], [7, 3], [3, 5]])
    assert test2 == 10
    
    test3 = sol.maximumWealth(accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]])
    assert test3 == 17
    