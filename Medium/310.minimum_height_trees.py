'''
https://leetcode.com/problems/minimum-height-trees/?envType=daily-question&envId=2024-04-23
'''

from collections import defaultdict

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph = defaultdict(list)
        for from_node, to_node in edges:
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)

        leaves = []
        new_leaves = []
        in_degree = []
        for start_node in range(n):
            if len(graph[start_node]) == 1:
                leaves.append(start_node)
            in_degree.append(len(graph[start_node]))

        num_nodes = n
        while num_nodes > 2:
            for leaf in leaves:
                for adj_leaf in graph[leaf]:
                    in_degree[adj_leaf] -= 1
                    if in_degree[adj_leaf] == 1:
                        new_leaves.append(adj_leaf)

            num_nodes -= len(leaves)
            leaves = new_leaves[:]
            new_leaves = []

        return leaves


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findMinHeightTrees(n = 4, edges = [[1, 0], [1, 2], [1, 3]])
    assert test1 == [1]
    
    test2 = sol.findMinHeightTrees(n = 6, edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
    assert test2 == [3, 4]
    