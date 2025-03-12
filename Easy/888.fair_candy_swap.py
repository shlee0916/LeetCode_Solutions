'''
https://leetcode.com/problems/fair-candy-swap/description/
'''

from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2
        
        for candy in set(bobSizes):
            if diff + candy in set(aliceSizes):
                return [diff + candy, candy]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.fairCandySwap(aliceSizes = [1, 1], bobSizes = [2, 2])
    assert test1 == [1, 2]

    test2 = sol.fairCandySwap(aliceSizes = [1, 2], bobSizes = [2, 3])
    assert test2 == [1, 2]

    test3 = sol.fairCandySwap(aliceSizes = [2], bobSizes = [1, 3])
    assert test3 == [2, 3]
