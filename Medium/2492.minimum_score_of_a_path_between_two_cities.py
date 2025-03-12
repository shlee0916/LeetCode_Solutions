'''
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for start, end, length in roads:
            graph[start][end] = graph[end][start] = length

        res = float("inf")
        que = [1]
        visit = set([1])
        while que:
            cur_node = que.pop(0)
            for destination, length in graph[cur_node].items():
                if destination not in visit:
                    que.append(destination)
                    visit.add(destination)
                res = min(res, length)

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minScore(n = 4, roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]])
    print(test1, 5)
    assert test1 == 5

    test2 = sol.minScore(n = 4, roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]])
    print(test2, 2)
    assert test2 == 2
    