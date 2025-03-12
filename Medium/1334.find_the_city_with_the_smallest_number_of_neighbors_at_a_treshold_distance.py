'''
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
'''

from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float("inf")] * n for _ in range(n)]
        for from_city, to_city, dist in edges:
            graph[from_city][to_city] = dist
            graph[to_city][from_city] = dist

        for node in range(n):
            graph[node][node] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        ans_cand = {sum(dist <= distanceThreshold for dist in graph[idx]): idx for idx in range(n)}

        return ans_cand[min(ans_cand)]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findTheCity(n = 4, edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold = 4)
    assert test1 == 3

    test2 = sol.findTheCity(n = 5, edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold = 2)
    assert test2 == 0
    