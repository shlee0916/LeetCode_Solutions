'''
https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
'''

from heapq import heapify, heappop, heappush
from math import sqrt

from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)

        for _ in range(k):
            new_pile = heappop(heap)
            heappush(heap, -int(sqrt(-new_pile)))

        return -sum(heap)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.pickGifts(gifts = [25, 64, 9, 4, 100], k = 4)
    assert test1 == 29

    test2 = sol.pickGifts(gifts = [1, 1, 1, 1], k = 4)
    assert test2 == 4
    