'''
https://leetcode.com/problems/path-with-maximum-probability/description/
'''

from math import log2
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [set() for _ in range(n)]
        for (depart, arrive), prob in zip(edges, succProb):
            graph[depart].add((arrive, log2(1/prob)))
            graph[arrive].add((depart, log2(1/prob)))

        dist = [float("inf") for _ in range(n)]
        dist[start] = 0

        heap = [(0, start)]
        while heap:
            cur_prob, cur_edge = heappop(heap)

            for next_edge, next_prob in graph[cur_edge]:
                if dist[cur_edge] + next_prob < dist[next_edge]:
                    dist[next_edge] = dist[cur_edge] + next_prob
                    heappush(heap, (dist[next_edge], next_edge))
        
        return 1 / (2 ** dist[end])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxProbability(n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.2], start = 0, end = 2)
    assert round(test1, 6) == 0.2500
    
    test2 = sol.maxProbability(n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.3], start = 0, end = 2)
    assert round(test2, 6) == 0.3000
    
    test3 = sol.maxProbability(n = 3, edges = [[0, 1]], succProb = [0.5], start = 0, end = 2)
    assert round(test3, 6) == 0.0000
    