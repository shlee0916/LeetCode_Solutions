'''
https://leetcode.com/problems/k-closest-points-to-origin/description/
'''

from heapq import heapify, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for idx, (x, y) in enumerate(points):
            heap.append([x * x + y * y, idx])
        
        heapify(heap)

        result = []
        for _ in range(k):
            _, idx = heappop(heap)
            result.append(points[idx])

        return result


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.kClosest(points = [[1, 3], [-2, 2]], k = 1)
    assert test1 == [[-2, 2]]

    test2 = sol.kClosest(points = [[3, 3], [5, -1], [-2, 4]], k = 2)
    assert test2 == [[3, 3], [-2, 4]]
    