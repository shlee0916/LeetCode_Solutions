'''
https://leetcode.com/problems/is-graph-bipartite/description/
'''

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        red = 1
        color_map = {}

        def dfs(start_node: int):
            for conn_node in graph[start_node]:
                if conn_node in color_map:
                    if color_map[conn_node] == color_map[start_node]:
                        return False
                
                else:
                    color_map[conn_node] = -color_map[start_node]
                    if not dfs(conn_node):
                        return False

            return True

        for start_node in range(len(graph)):
            if start_node not in color_map:
                color_map[start_node] = red
                if not dfs(start_node):
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.isBipartite(graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert test1 == False

    test2 = sol.isBipartite(graph = [[1, 3], [0, 2], [1, 3], [0, 2]])
    assert test2 == True
    