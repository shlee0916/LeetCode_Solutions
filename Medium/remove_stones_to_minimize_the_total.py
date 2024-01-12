'''
https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heappush(heap, -pile)

        for _ in range(k):
            heappush(heap, heappop(heap) // 2)

        return -sum(heap)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minStoneSum(piles = [5, 4, 9], k = 2)
    assert test1 == 12

    test2 = sol.minStoneSum(piles = [4, 3, 6, 7], k = 3)
    assert test2 == 12
    