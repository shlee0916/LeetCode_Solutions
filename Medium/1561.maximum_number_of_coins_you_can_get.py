'''
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
'''

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        piles_len = len(piles)

        return sum(piles[1 : -(piles_len // 3) : 2])
    
    # One-liner
    def maxCoins_one(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3 :: 2])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxCoins(piles = [2, 4, 1, 2, 7, 8])
    test1_one = sol.maxCoins_one(piles = [2, 4, 1, 2, 7, 8])
    assert test1 == 9
    assert test1_one == 9
    
    test2 = sol.maxCoins(piles = [2, 4, 5])
    test2_one = sol.maxCoins_one(piles = [2, 4, 5])
    assert test2 == 4
    assert test2_one == 4
    
    test3 = sol.maxCoins(piles = [9, 8, 7, 6, 5, 1, 2, 3, 4])
    test3_one = sol.maxCoins_one(piles = [9, 8, 7, 6, 5, 1, 2, 3, 4])
    assert test3 == 18
    assert test3_one == 18
    