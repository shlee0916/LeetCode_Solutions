'''
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
'''

from collections import defaultdict

from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for from_node, to_node in edges:
            graph[from_node].append(to_node)

        ancestors = [[] for _ in range(n)]

        def dfs(parents, cur_node): 
            for child in graph[cur_node]:
                if ancestors[child] and ancestors[child][-1] == parents:
                    continue

                ancestors[child].append(parents)
                dfs(parents, child)

        for node in range(n):
            dfs(node, node)

        return ancestors


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getAncestors(n = 8, edges = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]])
    assert test1 == [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

    test2 = sol.getAncestors(n = 5, edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    assert test2 == [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
