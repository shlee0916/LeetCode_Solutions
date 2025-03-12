'''
https://leetcode.com/problems/maximal-network-rank/description/
'''

from collections import defaultdict

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)

        for from_city, to_city in roads:
            graph[from_city].add(to_city)
            graph[to_city].add(from_city)

        ans = 0
        for from_city in range(n):
            for to_city in range(from_city + 1, n):
                ans = max(ans, len(graph[from_city]) + len(graph[to_city]) - (from_city in graph[to_city]))

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximalNetworkRank(n = 4, roads = [[0, 1], [0, 3], [1, 2], [1, 3]])
    assert test1 == 4
    
    test2 = sol.maximalNetworkRank(n = 5, roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]])
    assert test2 == 5
    
    test3 = sol.maximalNetworkRank(n = 8, roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]])
    assert test3 == 5
    