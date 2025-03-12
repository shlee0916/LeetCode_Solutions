'''
https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=daily-question&envId=2023-09-15
'''

from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        ans = 0
        length = len(points)
        seen = set()
        vertices = [(0, (0, 0))]

        while len(seen) < length:
            dist, (edge_x, edge_y) = heappop(vertices)

            if edge_y in seen:
                continue

            ans += dist
            seen.add(edge_y)

            for idx in range(length):
                if idx not in seen and idx != edge_y:
                    heappush(vertices, (manhattan(points[idx], points[edge_y]), (edge_y, idx)))

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minCostConnectPoints(points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
    assert test1 == 20
    
    test2 = sol.minCostConnectPoints(points = [[3, 12], [-2, 5], [-4, 1]])
    assert test2 == 18
    