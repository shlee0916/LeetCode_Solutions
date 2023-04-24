'''
https://leetcode.com/problems/last-stone-weight/description/
'''

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap_stones = [-stone for stone in stones]
        heapify(heap_stones)
        while len(heap_stones) > 1:
            diff = heappop(heap_stones) - heappop(heap_stones)
            if diff:
                heappush(heap_stones, diff)
            
        return -heap_stones[0] if heap_stones else 0


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.lastStoneWeight(stones = [2, 7, 4, 1, 8, 1])
    assert test1 == 1

    test2 = sol.lastStoneWeight(stones = [1])
    assert test2 == 1
